#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from cards import Deck,Library,Hand

DATAFILE='testdata.csv'

deck = Deck(DATAFILE)
library = Library(deck)
hand = library.getHand()


turn = 0 # how many turns we have "played"
numMana = 0 # how much many we have played

# need something to keep track of how many cards were played each turn
cardsPerTurn = np.array([], dtype=np.int8)
landPerTurn = np.array([], dtype=np.int8)
totalManaPerTurn = np.array([], dtype=np.int8)
freeManaPerTurn = np.array([], dtype=np.int8)
cardsAtEndOfTurn = np.array([], dtype=np.int8)


def printcurrenthand(hand):
    print("Current hand: ")
    print(hand)

# will eventually need to sort out if you start first or your opponent does
while turn < 20:
    print("Starting turn %i ..." % (turn + 1))

    cardsPerTurn = np.append(cardsPerTurn, 0)
    landPerTurn = np.append(landPerTurn, 0)
    freeManaPerTurn = np.append(freeManaPerTurn, 0)

    # draw
    hand = np.append(hand, library[0])
    print("Drawing a card:")
    print(library[0])
    library = library[1:]
    hand = np.sort(hand)

    printcurrenthand(hand)

    # play a land if you can
    if hand[0] == 0:
        print("Playing a land")
        numMana += 1
        hand = hand[1:]
        cardsPerTurn[-1] += 1
        landPerTurn[-1] += 1
        printcurrenthand(hand)
    print("Current mana count:")
    print(numMana)
    totalManaPerTurn = np.append(totalManaPerTurn, numMana)

    # which individual cards could be played?
    # will need to aventually take into account the chance
    #                     the player doesn't want to play a card?
    freeMana = numMana
    canplay = np.logical_and(hand > 0, hand <= freeMana)
    while freeMana > 0 and np.sum(canplay) > 0:
        print("Untapped mana:")
        print(freeMana)

        # choose a card to play at random from those that can be played
        k = np.flatnonzero(canplay == True)
        choice = np.random.choice(k)
        print("Could play one of:")
        print(hand[canplay])

        # play that card
        # update freeMana
        freeMana -= hand[choice]
        print("Playing: ")
        print(hand[choice])
        cardsPerTurn[-1] += 1

        # remove card from hand
        hand = np.append(hand[0:choice], hand[choice+1:])
        printcurrenthand(hand)
        
        # update cards that could be played this turn
        canplay = np.logical_and(hand > 0, hand <= freeMana)
    if freeMana == 0:
        print("No mana left to play a card, continuing turn")
    elif np.sum(canplay) == 0:
        print("Untapped mana:")
        print(freeMana)
        print("No cards that can be played this turn")

    freeManaPerTurn[-1] = freeMana
    cardsAtEndOfTurn = np.append(cardsAtEndOfTurn, len(hand))

    # discard at random
    if len(hand) > 7:
        choice = np.random.choice(np.arange(0, len(hand)))
        hand = np.append(hand[0:choice], hand[choice+1:])
        print("Hand is too large, discarding a card")
        printcurrenthand(hand)

    turn += 1
    print("End of turn")
    print("")

print(library)
print(cardsPerTurn)
print(landPerTurn)
print(freeManaPerTurn)
print(cardsAtEndOfTurn)

x = np.arange(1, len(cardsPerTurn)+1)
plt.plot(x, cardsPerTurn, '-bo', x, landPerTurn, '-mh', x, totalManaPerTurn, '-cD', x, freeManaPerTurn, '-rs', x, cardsAtEndOfTurn, '-g^')
plt.axis([0, 21, 0, 10])
plt.xlabel('Turn number')
plt.ylabel('Numer of...')
plt.legend(['Cards played per turn', 'Lands played per turn', 'Mana available at start of turn', 'Untapped mana at end of turn', 'Cards left in hand'])
# that this is the way to do this is rediculous, but remove decimals on x-axis tick labels
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%i'))

#plt.show()
plt.savefig('output.png', dpi=180)
