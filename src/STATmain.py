from tkinter import *
from STATboard import Board
from STATutil import Utility

def updateBoards():
    pass

counter = 0
tests = 20
numBoards = 6
boardsWinList = [0] * numBoards

numCalls = 0

# repeatedly run the game and save the results
while counter < tests:

    root = Tk()
    boardsList = []
    for i in range(0, numBoards):
        boardsList.append(Board(root, i))

    numCalls += Utility.completeGame(boardsList)

    counter += 1
    for i in range(numBoards):
        if i in Utility.checkWinner(boardsList):
            boardsWinList[i] += 1

# generate headers for output  'B0  B1 ... B10' and so on
headerString = "Boards: "
for i in range(numBoards):
    headerString += "B%d   " % i
print(headerString)

# record the percentage of games won by each board
winPercentages = []
for i in range(numBoards):
    winPercentages.append(boardsWinList[i] / tests * 100)

# create the output string to display percentage of games won by each board
winString = "Wins:   "
for i in range(numBoards):
    winString += "%d%%  " % winPercentages[i]

# display the results
print(winString)
print("Average Number of Calls: " + str(numCalls / tests))
