#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

from cards import Deck,Library,Hand

# data file that holds the deck we're investigating
DATAFILE='testdata.csv'

# the chance as 1/ODDSOFSKIP per turn that we don't play anything
ODDSOFSKIP=10

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



# will eventually need to sort out if you start first or your opponent does
while turn < 21:
    print("Starting turn %i ..." % (turn + 1))

    cardsPerTurn = np.append(cardsPerTurn, 0)
    landPerTurn = np.append(landPerTurn, 0)
    freeManaPerTurn = np.append(freeManaPerTurn, 0)

    # draw
    hand.addCard(library.draw())
    hand.print()

    # play a land if you can
    if hand.hasLand():
        hand.playCard(0)
        numMana += 1
        cardsPerTurn[-1] += 1
        landPerTurn[-1] += 1
        hand.print()
    print("Current mana count: %i" % numMana)
    totalManaPerTurn = np.append(totalManaPerTurn, numMana)

    # which individual cards could be played?
    # will need to aventually take into account the chance
    #                     the player doesn't want to play a card?
    freeMana = numMana
    canplay = hand.canPlay(freeMana)
    while freeMana > 0 and np.sum(canplay) > 0:
        print("Untapped mana: %i" % freeMana)
        print("Could play one of:")
        hand.print(canplay)

        # do we want to play a card this turn?
        if ODDSOFSKIP == 0 or np.random.choice(np.append(0, np.ones(ODDSOFSKIP-1, dtype=np.int8))) == 1:
            # choose a card to play at random from those that can be played
            choice = np.random.choice(np.flatnonzero(canplay == True))
            # play that card
            # update freeMana
            # remove card from hand
            freeMana -= hand.playCard(choice)
            cardsPerTurn[-1] += 1
            hand.print()
            
            # update cards that could be played this turn
            canplay = hand.canPlay(freeMana)
        else:
            print("Declining to play a card this turn")
            break
    if freeMana == 0:
        print("No mana left to play a card, continuing turn")
    elif np.sum(canplay) == 0:
        print("Untapped mana: %i" % freeMana)
        print("No cards that can be played this turn")

    freeManaPerTurn[-1] = freeMana

    # discard at random
    if hand.size() > 7:
        choice = np.random.choice(np.arange(0, hand.size()))
        hand.playCard(choice, True)
        print("Hand is too large, discarding a card")
        hand.print()

    cardsAtEndOfTurn = np.append(cardsAtEndOfTurn, hand.size())

    turn += 1
    print("End of turn")
    print("")

library.print()
print(cardsPerTurn)
print(landPerTurn)
print(freeManaPerTurn)
print(cardsAtEndOfTurn)

x = np.arange(1, len(cardsPerTurn)+1)
plt.plot(x, cardsPerTurn, '-bo', x, landPerTurn, '-mh', x, totalManaPerTurn, '-cD', x, freeManaPerTurn, '-rs', x, cardsAtEndOfTurn, '-g^')
plt.axis([0, len(cardsPerTurn)+1, 0, 12])
plt.xticks(x[0::2])
plt.xlabel('Turn number')
plt.ylabel('Numer of...')
plt.legend(['Cards played per turn', 'Lands played per turn', 'Mana available at start of turn', 'Untapped mana at end of turn', 'Cards left in hand'])
# that this is the way to do this is rediculous, but remove decimals on x-axis tick labels
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%i'))

#plt.show()
plt.savefig('output.png', dpi=180)
