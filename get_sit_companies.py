#!/usr/bin/env python

import csv
import sys
import re
from tabulate import tabulate

def getCsv(path):
    match = re.search(r'^.+\.csv', path)
    rows = []
    if match:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                temp = []
                temp.append(row['Name of Company'])
                temp.append(row['Address'])
                rows.append(temp)
    return rows

def getCompanies(file):
    companies = {}
    for row in file:
        if row[0] not in companies:
            companies[row[0]] = row[1]
        continue
    return companies

def outText(data):
    out = data.items()
    data = out
    with open('SIT.txt', 'w') as f:
        f.write('SIT Companies (2022)\n')
        f.write(tabulate(data))
        #for key, value in data.items():
        #    f.write('Name: {} \t\t Address: {}\n'.format(key,value))

def main():
    filename = sys.argv[1]
    csvData = getCsv(filename)
    companies = getCompanies(csvData)
    outText(companies)

if __name__ == '__main__':
    main()
