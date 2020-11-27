# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for revreports Project
"""

from os.path import split
import pandas as pd
import datetime
import revreports
# import pdb; pdb.set_trace()

ACTUALS = '../revreports/data/Actuals/2020_seg'
TODAY = datetime.datetime.today().strftime('%m-%d-%y')

def convert_seg_stat(date = TODAY):
    # need file name and date to add to report
    '''Enter date as format mm-dd-yy '''
    file_date = date.replace('-', '_')
    folder_source, _ = split(revreports.__file__)
    df = pd.read_csv(f'{folder_source}/data/{file_date}/segment_stat.txt', sep="\t", engine='python', skipfooter=2,
                 usecols=['GRP2_CODE', 'ROOMS_DAY', 'ROOM_REV_DAY'])

    df.columns = ['Code', 'Res', 'Rev']
    df['Date'] = date
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] = df['Date'] - pd.DateOffset(1)
    df = df[['Date', 'Code', 'Rev', 'Res']]
    file = f'{folder_source}/data/seg_stat_{file_date}.csv'
    df.to_csv(file, header=False, index=False)
    return file


def convert_seg_res(date = TODAY):
    file_date = date.replace('-', '_')
    folder_source, _ = split(revreports.__file__)

    df = pd.read_csv(f'{folder_source}/data/{file_date}/segment_res.txt', sep="\t",
                 usecols=['RESERVATION_DATE', 'MARKET_CODE', 'TOTAL_REVENUE','PRINT_NO_OF_ROOMS' ],
                engine='python', skipfooter=2, parse_dates=['RESERVATION_DATE'])

    df.columns = ['Date', 'Code', 'Rev', 'Res']
    file = f'{folder_source}/data/seg_res.{file_date}.csv'
    df.to_csv(file, index=False)
    return file


def convert_source_stat(date):
    file_date = date.replace('/', '_')
    df = pd.read_csv(f'../revreports/data/stat/source_stat_{file_date}.txt', sep="\t", engine='python', skipfooter=2,
                 usecols=['GRP2_CODE', 'ROOMS_DAY', 'ROOM_REV_DAY'])

    df.columns = ['Code', 'Res', 'Rev']
    df['Date'] = date
    # Saving in it's own location or with segment?
    df.to_csv(actuals, mode='a', header=False, index=False)

def convert_source_res(date):
    df = pd.read_csv('../revreports/data/11_23_20/segment_res.txt', sep="\t",
                 usecols=['RESERVATION_DATE', 'MARKET_CODE', 'TOTAL_REVENUE','PRINT_NO_OF_ROOMS'],
                engine='python', skipfooter=2)#, parse_dates=['RESERVATION_DATE'])

    df.columns = ['Date', 'Code', 'Rev', 'Res']
    # where do these get saved
    df.to_csv(date, index=False)





if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import revreports
    # folder_source, _ = split(revreports.__file__)
    # df = pd.read_csv('{}/data/data.csv.gz'.format(folder_source))
    # clean_data = clean_data(df)
    # print(' dataframe cleaned')
