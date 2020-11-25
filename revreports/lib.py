# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for revreports Project
"""

from os.path import split
import pandas as pd
import datetime

pd.set_option('display.width', 200)


def convert_seg_stat(data):
    pass

def convert_seg_res(data):
    pass

def convert_source_stat(data):
    pass

def convert_source_res(data):
    pass




if __name__ == '__main__':
    # For introspections purpose to quickly get this functions on ipython
    import revreports
    # folder_source, _ = split(revreports.__file__)
    # df = pd.read_csv('{}/data/data.csv.gz'.format(folder_source))
    # clean_data = clean_data(df)
    # print(' dataframe cleaned')
