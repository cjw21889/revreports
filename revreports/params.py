
LOCAL_PATH = 'nov22.csv'
BUCKET_NAME = 'revreports'
BUCKET_FOLDER = 'actuals_20'
PROJECT_ID = 'revreports'
TOTAL_ACCTUALS = 'actuals_2020.csv'
CURRENT_ACCTUALS = 'actuals_2020.csv'

MONTHS ={'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6,'July':7,
          'August':8,'September':9,'October':10, 'November':11, 'December':12}

CODES = ['GS', 'SP', 'HSE', 'GE', 'PK', 'OT', 'RA', 'GC', 'GV', 'CO', 'WH', 'GL', 'CS', 'NG', 'OP']

CONDENSED_SEG = {'CO': 'Comp', 'CS': 'Consortia', 'GC': 'Group', 'GE': 'Group',
                 'GL': 'Group', 'GS': 'Group', 'GV': 'Corporate', 'HSE': 'Comp',
                 'NG': 'Corporate', 'OP': 'OTA', 'OT': 'OTA', 'PK': 'Direct',
                 'RA': 'Direct', 'SP': 'Direct', 'WH': 'Wholesale'}

FULL_SEG = {'CO': 'Comp', 'CS': 'Consortia', 'GC': 'Group', 'GE': 'Group',
            'GL': 'Group', 'GS': 'Group', 'GV': 'Government', 'HSE': 'House',
            'NG': 'Corporate', 'OP': 'Opaque', 'OT': 'OTA', 'PK': 'Package',
            'RA': 'BAR', 'SP': 'Special', 'WH': 'Wholesale'}

ROOMCOUNT = 249
