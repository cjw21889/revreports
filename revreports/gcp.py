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

def download_from_gcp():
    creds = get_credentials()
    client = storage.Client(credentials=creds, project=PROJECT_ID).bucket(BUCKET_NAME)
    storage_location = 'actuals_20/actuals_2020.csv'

    blob = client.blob(storage_location)
    blob.download_to_filename('actuals.csv')



if __name__ == '__main__':
    download_from_gcp()
