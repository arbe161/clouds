#allows use of csv files
import csv

import os
#for CLA
import sys
import argparse
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
    
    n_args = len(sys.argv)
    if n_args == 1:
        print('please include name')
        sys.exit()        
        
    if n_args == 3:
        year = sys.argv[2]
        
    name = sys.argv[1]
    with open('list.csv', 'r') as fp:
        s = fp.read()
    
    missing = []
    
    if name not in s:
        missing.append(name)
        
    print(missing)
    with open('list.csv', 'a') as fp:
        fp.writelines(value + '\n' for value in missing)
else: 
    print('csv file created')
    with open('list.csv', 'w') as fp:
        fp.writelines(header)