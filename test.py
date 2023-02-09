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
args = parser.parse_args()

if args.delete == True:
    print('Resetting CSV file')
    os.remove(path)

dict_toAdd = {'Name': [], 'Year Formed':[]}

#check if file exists
#check if value already exists
if os.path.exists('list.csv'):
    print('file exists')
    df_original = pd.read_csv(path)
    print(df_original)
else:
    print('creating new csv')
    df_original = pd.DataFrame(dict_toAdd)
    print(df_original)

name_toAdd = input('Please input a name to add: ')
if name_toAdd not in df_original.Name.values:
    print('Name: %s is not in file' % name_toAdd)
    dict_toAdd['Name'].append(name_toAdd)
    year_formed = int(input('Please enter and integer for the year formed: '))
    dict_toAdd['Year Formed'].append(year_formed)
    print(dict_toAdd)
else:
    print('Name: %s already in file. Exiting...' % name_toAdd)
    exit()

df_toAdd = pd.DataFrame(dict_toAdd)
print(df_toAdd)
ret = pd.concat([df_original, df_toAdd])
print(ret)
#ret.reset_index(drop=True)
print(ret)

csv_data = ret.to_csv(path)
#with open('list.csv', 'a') as fp:
#    fp.writelines(value + '\n' for value in missing)

#df = pd.DataFrame(my_df)
#my_df = pd.Series(header)
#csv_data = my_df.to_csv('list.csv')
#with open('list.csv', 'w') as fp:
#    fp.writelines(header)    
# #n_args = len(sys.argv)
    #if n_args == 1:
    #    print('please include name')
    #    sys.exit()        
    #name = sys.argv[1]
    #print(name)
    #if n_args == 3:
    #    year = sys.argv[2]
    
    
    #with open('list.csv', 'r') as fp:
    #    s = fp.read()