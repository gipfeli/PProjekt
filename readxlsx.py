# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:17:10 2017

@author: Admin
"""

# Library to read/convert Excel to CSV file.
from xlrd import open_workbook
import csv

def readData():
    dataname = 'ioTable.xlsx'
    wb = open_workbook(dataname)
 
    i = 0 # Sheet needed to update, array index!
    sheet = wb.sheet_by_index(i)
    print sheet.name
    with open("%s.csv" %(sheet.name.replace(" ","")), "w") as file:
        writer = csv.writer(file, delimiter = ",")
        print sheet, sheet.name, sheet.ncols, sheet.nrows
     
    #        header = [cell.value for cell in sheet.row(0)]                     # Remove if need header
    #        writer.writerow(header)
     
        for row_idx in range(0, sheet.nrows):                               
            row = [int(cell.value) if isinstance(cell.value, int)           # If the row is int => int, or float => float, or else, string
                else float(cell.value) if isinstance(cell.value, float)     # The easiest way, is simply call cell.value, and get everything in float.
                else cell.value
                   for cell in sheet.row(row_idx)]
            writer.writerow(row)
            print row
            
def search():
    search = raw_input('Insert Output key here: ')
    data = csv.reader(open('IOTable.csv'))
    for row in data:
        if search == row[3]:
            print row[3], row[4]
    
if __name__ == "__main__":
           
    readData()
    search()
    
