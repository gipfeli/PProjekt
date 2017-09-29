# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 19:46:44 2017

@author: Admin
"""

import csv

def executeFunc(ID):
    print "This is a test # %s" %ID

def getInputID():
    with open("IOTable.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            return row[0]
        
if __name__ == "__main__":
    executeFunc(getInputID())