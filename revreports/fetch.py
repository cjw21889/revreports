import pandas as pd
import numpy as np
from revreports.params import BUCKET_NAME, BUCKET_FOLDER, CODES



def preprocess_otb(df, actuals=None, merge=False):
    # df.Date = pd.to_datetime(df.Date)
    df = df[df.Code.isin(CODES)].reset_index(drop=True)
    df.Rev = df.Rev.astype(np.int32)
    if merge:
        df = pd.concat([actuals[actuals.Date < df.loc[0]['Date']], df])
        df.reset_index(drop=True, inplace=True)

    return df


def get_data():
    ''' returns 4 data frames: past actuals, current otb, yesterday otb, past df'''
    dates = ['Date']
    d_types = {'Res': 'int32', 'Rev': 'float32'}
    # d_types = {'Res': 'int32', 'Rev': 'float32', 'Code':'category'}
    actuals = preprocess_otb(pd.read_csv('data/actuals.csv', parse_dates=dates, dtype=d_types))
    current_df = preprocess_otb(pd.read_csv('data/otb-12-01.csv', parse_dates=dates,\
                                dtype=d_types),  actuals=actuals, merge=True)
    yesterday_df = preprocess_otb(pd.read_csv('data/otb-11-30.csv',parse_dates=dates,\
                                dtype=d_types), actuals=actuals, merge=True)
    past_df = preprocess_otb(pd.read_csv('data/otb-11-23.csv',parse_dates=dates,\
                                dtype=d_types), actuals=actuals, merge=True)
    return actuals, current_df, yesterday_df, past_df

