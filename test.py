#allows use of csv files
import csv

import os
#for CLA
import sys

n = len(sys.argv)
name = sys.argv[1]
#year = sys.argv[2]

#check if file exists
#check if value already exists
if os.path.exists('list.csv'):
    with open('list.csv', 'r') as fp:
        s = fp.read()
    
    missing = []
    
    if name not in s:
        missing.append(name)
        
    print(missing)
    with open('list.csv', 'a') as fp:
        fp.writelines(value + '\n' for value in missing)
else: 
    with open('list.csv', 'w') as fp:
        fp.writelines(name + '\n')