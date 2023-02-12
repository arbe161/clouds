#allows use of csv files
import csv

import os
#for CLA
import sys
import argparse
import warnings
import pandas as pd

#potential global filter for numpy type disagreements between python and numpy/pandas
#warnings.simplefilter(action='ignore', category=FutureWarning)

path = 'list.csv'

if os.path.exists(path):
    csv_exists = True
else:
    csv_exists = False

parser = argparse.ArgumentParser(description='build and alter database')
parser.add_argument('-a', '--add', action='store_true', help='add values to csv file')
parser.add_argument('-v', '--view', action='store_true', help='view dataframes during execution')
parser.add_argument('-d', '--delete', action='store_true', help='delete saved csv file')
args = parser.parse_args()

if args.delete == True:
    if csv_exists:
        print('Deleting previous CSV file')
        os.remove(path)
        csv_exists = False
    else:
        print('Can\'t delete file that does not exist, exiting')
        exit()

if args.add == True:
    dict_toAdd = {'Name': [], 'Year Formed':[]}
    if csv_exists:
        df_original = pd.read_csv(path)
        if args.view == True:
            print('Prior CSV loaded \n---------------------------- \n %s' % df_original)
    else:
        print('creating new csv')
        df_original = pd.DataFrame(dict_toAdd)

    
    continue_input = True
    while continue_input:
        ignore = False
        name_toAdd = input('Please input a name to add: ')
        with warnings.catch_warnings():
            warnings.simplefilter(action='ignore', category=FutureWarning)
            if name_toAdd in df_original.Name.values:
                print('\n Name: %s is in original csv.' % name_toAdd)
                ignore = True
        if name_toAdd in dict_toAdd['Name']:
            print('\n Name: %s has already been added in this session.' % name_toAdd)
            ignore = True
        if ignore: 
            print('Input ignored\n')
            continue
        else:
            print('Name: %s is not in file' % name_toAdd)
            dict_toAdd['Name'].append(name_toAdd)
            year_formed = int(input('Please enter and integer for the year formed: '))
            dict_toAdd['Year Formed'].append(year_formed)
            
            
        flag = input('Enter more information? --type N to exit--')
        if flag == 'N':
            continue_input = False
            

    df_toAdd = pd.DataFrame(dict_toAdd)
    print('\nDataFrame to add to original file \n ---------------------------------- \n %s \n' % df_toAdd)
    ret = pd.concat([df_original, df_toAdd])
    ret['Year Formed'] = ret['Year Formed'].astype(int)
    if args.view == True:
            print('Final CSV- indexing may be incorrect\n---------------------------- \n %s' % ret)

    csv_data = ret.to_csv(path, index=False)
