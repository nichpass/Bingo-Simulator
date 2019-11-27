from random import randint
from string import ascii_lowercase

# using 64 possible tile values across the 75 tiles (25 tiles in each 5x5 board)
tileValues = []
for i in range(1, 4):
    for char in ascii_lowercase:
            if not (i == 3 and char > 'l'):
                val = "%s%d" % (char, i)
                tileValues.append(val)


class Utility:

    @staticmethod
    def completegame(boards):
        while not any(board.hasBingo() for board in boards):
            Utility.singleIteration(boards)

    @staticmethod
    def singleIteration(boards):
        tileVal = Utility.genRandomTile()
        Utility.updateBoards(boards, tileVal)


    @staticmethod
    def genRandomTile():
        num = randint(0, 63)
        return tileValues[randint]


    @staticmethod
    def updateBoards(boards, tileVal):
        for board in boards:
            board.updateTiles(tileVal)

