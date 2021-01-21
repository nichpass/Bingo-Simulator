from tkinter import *
from board import Board
from util import Utility


# Utility.initHardware()

root = Tk()
root.geometry("1000x500")
root.title("BINGO Game")

bingoTitle = Label(root, text="BINGO", borderwidth=1)
bingoTitle.config(font=("Helvetica", 32))
bingoTitle.pack()

boardFrame = Frame(root)
board3 = Board(boardFrame, 3)
board2 = Board(boardFrame, 2)
board1 = Board(boardFrame, 1)

boardsList = [board1, board2, board3]

board1.boardFrame.pack(side=LEFT, expand=YES, padx=10)
board2.boardFrame.pack(side=LEFT, expand=YES, padx=10)
board3.boardFrame.pack(side=LEFT, expand=YES, padx=10)
boardFrame.pack()

# buttonFrame = Frame(root, pady=20)
# boardButton1 = Button(buttonFrame, text="Board 1", command=lambda: Utility.updateHardware(board1)).pack(side=LEFT)
# boardButton2 = Button(buttonFrame, text="Board 2", command=lambda: Utility.updateHardware(board2)).pack(side=LEFT)
# boardButton3 = Button(buttonFrame, text="Board 3", command=lambda: Utility.updateHardware(board3)).pack(side=LEFT)
# buttonFrame.pack()

gameButtonFrame = Frame(root)
singleIterButton = Button(gameButtonFrame, text="Call A Value", command=lambda: Utility.singleIteration(boardsList)).pack(side=LEFT)
finishGameButton = Button(gameButtonFrame, text="Call Until End", command=lambda: Utility.completeGame(boardsList)).pack(side=LEFT)
restartButton = Button(gameButtonFrame, text="Restart Game", command=lambda: Utility.restartGame(boardsList)).pack(side=LEFT)
gameButtonFrame.pack()

#root.protocol("WM_DELETE_WINDOW", lambda: Utility.turnOffLEDs(root))
root.protocol("WM_DELETE_WINDOW", lambda: root.destroy())
root.mainloop()
