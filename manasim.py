#!/usr/bin/env python
import csv
import numpy as np

DATAFILE='testdata.csv'

deck = np.array([], dtype=np.int8);

with open(DATAFILE, 'r') as csvfile:
    datareader = csv.reader(csvfile)

    i = 0
    for row in datareader:
        if i != 0:
            deck = np.append(deck, np.int8(row[1]))
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
#print(library)
#print(len(library))


turn = 0
numMana = 0
# need something to keep track of how many cards were played each turn

# will eventually need to sort out if you start first or your opponent does
while turn < 1:#20:
    # draw
    hand = np.append(hand, library[0])
    library = library[1:]
    hand = np.sort(hand)

    # play a land if you can
    if hand[0] == 0:
        numMana += 1
    hand = hand[1:]

    # which individual cards could be played?
    # multiple cards per turn will need to be handled at some point
    freeMana = numMana
    canplay = np.logical_and(hand > 0, hand <= numMana)
    while freeMana > 0 and np.sum(canplay) > 0:
        # choose a card to play at random from those that can be played
        k = np.flatnonzero(canplay == True)
        choice = np.random.choice(k)

        # play that card
        # update freeMana
        # update cards that could be played this turn
        # canplay = np.logical_and(hand > 0, hand <= numMana)
    print(canplay)

    # discard at random
    if len(hand) > 7:
        1
    turn += 1

#print(hand)
#print(library)
