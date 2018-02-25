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
