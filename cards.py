from csv import reader
import numpy as np

class Deck:
    def __init__(self, filename):
        self.cards = np.array([], dtype=np.int8)

        with open(filename, 'r') as csvfile:
            datareader = reader(csvfile)

            i = 0
            for row in datareader:
                if i != 0: # skip first line of file (row headings)
                    self.cards = np.append(self.cards, np.int8(row[1]))
                i += 1

    def print(self):
        print(self.cards)


class Library:
    def __init__(self, adeck):
        self.library = np.array(adeck.cards)
        # shuffle the library
        np.random.shuffle(self.library)

    def getHand(self):
        ahand = self.library[0:7]
        hand = Hand(ahand)
        self.library = self.library[7:]
        return hand

    def print(self):
        print(self.library)


class Hand:
    def __init__(self, ahand):
        self.hand = np.sort(ahand)

    def print(self):
        print(self.hand)
