import pandas as pd
from calendar import monthrange
pd.set_option('use_inf_as_na', True)
from revreports.params import CODES, ROOMCOUNT, MONTHS




def create_pickup(df1, df2):
    if len(df1) == len(df2):
        df1['Res p/u'] = df1.Res - df2.Res
        df1['Rev p/u'] = df1.Rev - df2.Rev
        # df1['ADR p/u'] = df1['Rev p/u'] / df1['Res p/u']

    # pu_df = df1.merge(df2, on=['Date', 'Code'], suffixes=['_t', '_p'])
    return df1


def create_day_view(df):
    df = df.groupby('Date', as_index=True)['Res', 'Rev', 'Res p/u', 'Rev p/u'].sum()
    df['ADR p/u'] = df['Rev p/u'] / df['Res p/u']
    df['ADR'] = df.Rev / df.Res
    df['Occ'] = 100 * (df.Res / ROOMCOUNT)
    df['|'] = '|'
    df = df.fillna(0)
    df = df.round(0)

    df = df[['Occ','Res', 'ADR', 'Rev', '|', 'Res p/u', 'ADR p/u','Rev p/u']]


    return df

def create_month_view(df):
    # df['Month'] = pd.to_datetime(df.Date, format='%B')
    df = df.groupby(df.Date.dt.month, as_index=False)['Res', 'Rev', 'Res p/u', 'Rev p/u'].sum()
    df['Month'] = list(MONTHS.keys())
    # df = df.reset_index('Month')
    df['ADR'] = df.Rev / df.Res
    df['ADR p/u'] = df['Rev p/u'] / df['Res p/u']
    df['|'] = '|'
    # df['Occ'] = df.Res / (monthrange(df.Date.dt.year, df.Date.dt.month) * ROOMCOUNT)
    df = df.fillna(0)
    df = df[['Month', 'Res', 'ADR', 'Rev', '|', 'Res p/u', 'ADR p/u', 'Rev p/u']]
    df = df.round(2)


    return df

