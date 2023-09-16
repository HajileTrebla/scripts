#!/usr/bin/env python

import sys 
import re
import pandas as pd

def getXlsx(path):
    xlsx_file = pd.read_excel(path) 
    return xlsx_file

def xlsxToCsv(file, output='output.csv'):
    file.to_csv(output,
                index = None,
                header = True)

def main():
    xlsx_file = getXlsx(sys.argv[1])
    m = re.search(r'^(.+).xls[sx]', sys.argv[1])
    if m:
        name = m.group(1) + '.csv' 
        xlsxToCsv(xlsx_file, name)
    else:
        xlsxToCsv(xlsx_file)

if __name__ == '__main__':
    main()
