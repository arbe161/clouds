#allows use of csv files
import csv

import os
#for CLA
import sys
import argparse
import pandas as pd

path = 'list.csv'
parser = argparse.ArgumentParser(description='build and alter database')
parser.add_argument('-d', '--delete', action='store_true')

header = ['Name', 'Year Formed']
args = parser.parse_args()

if args.delete == True:
    print('Resetting CSV file')
    os.remove(path)


#check if file exists
#check if value already exists
if os.path.exists('list.csv'):
    print('file exists')
    #n_args = len(sys.argv)
    #if n_args == 1:
    #    print('please include name')
    #    sys.exit()        
    #name = sys.argv[1]
    #print(name)
    #if n_args == 3:
    #    year = sys.argv[2]
    
    
    #with open('list.csv', 'r') as fp:
    #    s = fp.read()
    df = pd.read_csv(path)
    missing = []
    name_toAdd = input('Please input a name to add')
    
    if name_toAdd not in df.Name.values:
        print('Name: %s is not in file' % name_toAdd)
        missing.append(name_toAdd)
        year_formed = int(input('Please enter and integer for the year formed'))
        missing.append(year_formed)
        print(missing)
    else:
        print('Name: %s already in file. Exiting...' % name_toAdd)
        exit()
    series_toAdd = {}
    series_toAdd['Band'] = name_toAdd
    series_toAdd['Year Formed'] = year_formed
    ser = pd.Series(series_toAdd)
    pd.concat([df, ser])
    #df.loc[len(df)] = missing
    csv_data = df.to_csv(path)
    #with open('list.csv', 'a') as fp:
    #    fp.writelines(value + '\n' for value in missing)
else: 
    print('creating new csv')
    data = {'Name':['mbv', 'slowdive'], 'Year Formed':[2002, 3112]}
    df = pd.DataFrame(data)
    csv_data = df.to_csv(path)
    #df = pd.DataFrame(my_df)
    #my_df = pd.Series(header)
    #csv_data = my_df.to_csv('list.csv')
    #with open('list.csv', 'w') as fp:
    #    fp.writelines(header)