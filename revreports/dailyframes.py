import pandas as pd
pd.set_option('use_inf_as_na', True)
from revreports.params import CODES, ROOMCOUNT, MONTHS
from revreports.utils import dollar_format, occ_format, get_monthly_occ


def create_pickup(df1, df2):
    if len(df1) == len(df2):
        df1['Res p/u'] = df1.Res - df2.Res
        df1['Rev p/u'] = df1.Rev - df2.Rev
        # df1['ADR p/u'] = df1['Rev p/u'] / df1['Res p/u']

    # pu_df = df1.merge(df2, on=['Date', 'Code'], suffixes=['_t', '_p'])
    return df1


def create_day_view(df):
    df = df.groupby('Date', as_index=True)[['Res', 'Rev', 'Res p/u', 'Rev p/u']].sum()
    df.index = df.index.strftime('%A - %m/%d')
    df['ADR p/u'] = df['Rev p/u'] / df['Res p/u']
    df['ADR'] = df.Rev / df.Res
    df['Occ'] = 100 * (df.Res / ROOMCOUNT)
    df['|'] = '|'
    df = df.fillna(0)
    df = df.round(0)

    df = df[['Occ','Res', 'ADR', 'Rev', '|', 'Res p/u', 'ADR p/u','Rev p/u']]
    df['Occ'] = df['Occ'].apply(occ_format)
    for col in ['ADR', 'Rev', 'ADR p/u', 'Rev p/u']:
        df[col] = df[col].apply(dollar_format)

    return df


def create_month_view(df, year):
    df = df.groupby(df.Date.dt.month, as_index=False)[['Res', 'Rev', 'Res p/u', 'Rev p/u']].sum()
    df['Month'] = list(MONTHS.keys())
    df['ADR'] = df.Rev / df.Res
    df['ADR p/u'] = df['Rev p/u'] / df['Res p/u']
    df['|'] = '|'
    df['Occ'] = df.apply(lambda x: get_monthly_occ(x, year), axis=1)
    df = df.fillna(0)
    df = df[['Month', 'Occ','Res', 'ADR', 'Rev', '|', 'Res p/u', 'ADR p/u', 'Rev p/u']].set_index('Month')
    df['Occ'] = df['Occ'].apply(occ_format)
    for col in ['ADR', 'Rev', 'ADR p/u', 'Rev p/u']:
        df[col] = df[col].apply(dollar_format)
    return df

