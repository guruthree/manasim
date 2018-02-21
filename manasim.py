#!/usr/bin/env python
import csv
import numpy as np

DATAFILE='testdata.csv'

deck = np.array([]);

with open(DATAFILE, 'r') as csvfile:
    datareader = csv.reader(csvfile)

    i = 0
    for row in datareader:
        if i != 0:
            deck = np.append(deck, row[1])
        i += 1

print(deck)
