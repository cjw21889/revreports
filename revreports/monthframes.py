import pandas as pd
pd.set_option('use_inf_as_na', True)
from revreports.params import CODES, ROOMCOUNT, MONTHS
from revreports.utils import dollar_format

def seg_pickup(df):
    df = df.groupby('Code', as_index=True)['Res', 'Rev', 'Res p/u', 'Rev p/u'].sum()
    df['ADR p/u'] = df['Rev p/u'] / df['Res p/u']
    df['ADR'] = df.Rev / df.Res
    df['|'] = '|'
    df = df.fillna(0)
    df = df.round(0)

    df = df[['Res', 'ADR', 'Rev', '|', 'Res p/u', 'ADR p/u', 'Rev p/u']]
    for col in ['ADR', 'Rev', 'ADR p/u', 'Rev p/u']:
        df[col] = df[col].apply(dollar_format)

    return df

