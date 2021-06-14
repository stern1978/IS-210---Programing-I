#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Boroughs data."""

import json

Grades = {
    'A' : 100,
    'B' : 90,
    'C' : 80,
    'D' : 70,
    'F' : 60
}

csvpath = open('inspection_results.csv', 'r')
csvout = 'csv.txt'
jsonpath = open('green_markets.json', 'r')
jsonout = 'json.txt'


mydict={}
boro = {}
score = {}
def get_score_summary(self):
    for line in csvpath:
        parts = line.split(',')
        #filters out no grade
        if parts[10] in Grades:
            key = parts[0]
            value1 = parts[1]
            value2 = parts[10]
            mydict[key] = value1, value2
            grades = int(Grades[parts[10]])


            
            for b in mydict:
                boro[value1] = grades
        else:
            pass
        
    csvpath.close()
    print (boro)

def get_market_density(self):
    json.load(csvout)

def correlate_data(cvsout, jsonout, correlated):
    jason.dump('data', jsonpath)

    
if __name__ == '__main__':
    get_score_summary(csvpath)


