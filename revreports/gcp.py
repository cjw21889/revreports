import os
import json
from google.cloud import storage
from google.oauth2 import service_account
from revreports.params import BUCKET_NAME, PROJECT_ID


def get_credentials():
    credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    if '.json' in credentials_raw:
        credentials_raw = open(credentials_raw).read()
    creds_json = json.loads(credentials_raw)
    creds_gcp = service_account.Credentials.from_service_account_info(creds_json)
    return creds_gcp

def download_from_gcp(files):
    '''end a dictionary with gcp location as key and local dest as value '''
    creds = get_credentials()
    client = storage.Client(credentials=creds, project=PROJECT_ID).bucket(BUCKET_NAME)
    # iterate through file dictionary and save each needed file
    for k,v in files.items():
        blob = client.blob(k)
        blob.download_to_filename(v)


def upload_res(file, date, bucket=BUCKET_NAME, rm=False):
    client = storage.Client().bucket(bucket)
    storage_location = 'OTB_20/{}/{}'.format(date,
        'seg_res')
    blob = client.blob(storage_location)
    blob.upload_from_filename(file)
    print("=> res report uploaded to gs://{}/{}".format(BUCKET_NAME, storage_location))
    if rm:
        os.remove(file)
        print('file removed from local drive')

def merge_stat(file, date, bucket=BUCKET_NAME, rm=False):
    # setup client
    client = storage.Client().bucket(bucket)
    # hardcoded temp stat file - and upload it
    storage_location = 'actuals_20/seg_stat'
    blob = client.blob(storage_location)
    blob.upload_from_filename(file)
    location = "gs://{}/{}".format(BUCKET_NAME, storage_location)
    print("=> stat report uploaded to {}".format(location))

    # remove it locally
    if rm:
        os.remove(file)
        print('file removed from local drive')

    # hard coded running actuals for the year
    full_blob = client.blob("actuals_20/actuals_2020.csv")
    # set them in a list
    sources = [full_blob, blob]

    # set up destination to override running actuals after it merges with temp file
    destination = client.blob("actuals_20/actuals_2020.csv")
    destination.content_type = "text/csv"
    destination.compose(sources)

    # delet temp file from gcp
    blob.delete()
    print('actuals merged on gcp')

if __name__ == '__main__':
    # download_from_gcp(files = {'actuals_20/actuals_2020.csv': 'actuals.csv','OTB_20/11-23-20/seg_res': 'otb-11-23.csv','OTB_20/11-26-20/seg_res': 'otb-11-26.csv','OTB_20/11-27-20/seg_res': 'otb-11-27.csv'})
    pass
