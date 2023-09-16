#!/usr/bin/env python

import csv
import sys
import re

def getCsv(path):
    match = re.search(r'^.+\.csv', path)
    rows = []
    if match:
        with open(path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(row['Name of Company'])
    return rows

def getCompanies(file):
    companies = {}
    for row in file:
        if row not in companies:
            companies[row] = 0
        companies[row] += 1
    return companies

def outText(data):
    with open('SIT.txt', 'w') as f:
        f.write('SIT Companies (2022)\n')
        for key, value in data.items():
            f.write(key+'\n')

def main():
    filename = sys.argv[1]
    csvfile = getCsv(filename)
    companies = getCompanies(csvfile)
    outText(companies)

if __name__ == '__main__':
    main()
