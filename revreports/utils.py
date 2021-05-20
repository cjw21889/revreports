import pandas as pd
from calendar import monthrange


def dollar_format(x):
    if x >= 0:
        return "${0:,.0f}".format(x)
    return "-${0:,.0f}".format(abs(x))


def occ_format(x):
    return f"{int(x)}%"


def get_monthly_occ(x, year):
   return (x.Res / (monthrange(year, pd.to_datetime(x.Month, format='%B').month)[1] * ROOMCOUNT)) * 100
