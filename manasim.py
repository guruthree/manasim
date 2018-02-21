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

library = np.array(deck)

# shuffle the deck
np.random.shuffle(library)
#print(deck)
#print(library)
#print(len(library))

hand = library[0:7]
hand = np.sort(hand)
#print(hand)
library = library[7:]
print(library)
#print(len(library))


turn = 0
numMana = 0

# will eventually need to sort out if you start first or your opponent does
while turn < 20:
    # draw
    hand = np.append(hand, library[0])
    library = library[1:]
    hand = np.sort(hand)



    turn += 1

print(hand)
print(library)
