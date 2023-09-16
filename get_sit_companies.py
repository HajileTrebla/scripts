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
    companies = dict(sorted(companies.items()))
    return companies

def getCount(file):
    count = {}
    for row in file:
        if row[0] not in count:
            count[row[0]] = 0
        count[row[0]] += 1
        continue
    count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))
    return count

def outText(data, filename='SIT.txt'):
    out = data.items()
    data = out
    with open(filename, 'w') as f:
        f.write('SIT Companies (2022)\n')
        f.write(tabulate(data))

def main():
    filename = sys.argv[1]
    csvData = getCsv(filename)
    companies = getCompanies(csvData)
    count = getCount(csvData)
    outText(companies, 'companies.txt')
    outText(count, 'count.txt')
    #log
    print('Companies parsed successfully\n')
    print('Number of Companies: {}'.format(len(companies)))

if __name__ == '__main__':
    main()
