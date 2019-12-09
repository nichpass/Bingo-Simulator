from tkinter import *
from STATboard import Board
from STATutil import Utility

def updateBoards():
    pass

counter = 0
tests = 100
numBoards = 6
boardsWinList = [0] * numBoards

numCalls = 0

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

headerString = "Boards: "
for i in range(numBoards):
    headerString += "B%d   " % i
print(headerString)

winPercentages = []
for i in range(numBoards):
    winPercentages.append(boardsWinList[i] / tests * 100)

winString = "Wins:   "
for i in range(numBoards):
    winString += "%d%%  " % winPercentages[i]
print(winString)

'''print(tests,'Tests  ','B1', ' B2', ' B3')
print('Wins:','    ', b1wins,' ', b2wins,' ', b3wins)
p1 = str(round(100*b1wins/tests))
p2 = str(round(100*b2wins/tests))
p3 = str(round(100*b3wins/tests))
print('Win Rate:', p1+'%', p2+'%', p3+'%')'''

print("average num calls: " + str(numCalls / tests))
