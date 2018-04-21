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

    def draw(self):
        acard = self.library[0]
        print("Drawing a card: %i" % acard)
        self.library = self.library[1:]
        return acard

    def print(self):
        print(self.library)


class Hand:
    def __init__(self, ahand):
        self.hand = np.sort(ahand)

    def addCard(self, acard):
        ahand = np.append(self.hand, acard)
        self.hand = np.sort(ahand)

    def playCard(self, positioninhand, discard=False):
        acard = self.hand[positioninhand]
        if acard == 0 and not discard:
            print("Playing a land")
        else:
            if not discard:
                print("Playing: %i" % acard)
            else:
                print("Discarding: %i" % acard)
        self.hand = np.append(self.hand[0:positioninhand], self.hand[positioninhand+1:])
        return acard

    def hasLand(self):
        if self.hand[0] == 0:
            return True
        else:
            return False

    def canPlay(self, freeMana):
        return np.logical_and(self.hand > 0, self.hand <= freeMana)

    def size(self):
        return len(self.hand)

    def print(self, selection=None):
        if selection is None:
            print("Current hand: ")
            print(self.hand)
        else:
            print(self.hand[selection])
