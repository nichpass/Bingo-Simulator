from tkinter import *
from src.board import Board
from src.util import Utility

def updateBoards():
    pass

root = Tk()
root.geometry("500x500")
root.title("BINGO Game")

bingoTitle = Label(root, text="BINGO", borderwidth=1)
bingoTitle.config(font=("Helvetica", 32))
bingoTitle.pack()

board3 = Board(root, 3)
board2 = Board(root, 2)
board1 = Board(root, 1)

boardsList = [board1, board2, board3]

buttonFrame = Frame(root)
boardButton1 = Button(buttonFrame, text="Board 1", command=board1.focus).pack(side=LEFT)
boardButton2 = Button(buttonFrame, text="Board 2", command=board2.focus).pack(side=LEFT)
boardButton3 = Button(buttonFrame, text="Board 3", command=board3.focus).pack(side=LEFT)
buttonFrame.pack()

board1.render()
board2.render()
board3.render()

gameButtonFrame = Frame(root)
singleIterButton = Button(gameButtonFrame, text="Call a value", command=lambda: Utility.singleIteration(boardsList)).pack(side=LEFT)
finishGameButton = Button(gameButtonFrame, text="Call until end", command=updateBoards).pack(side=LEFT)
gameButtonFrame.place(relx=0.5, rely=0.9, anchor=S)

root.mainloop()

