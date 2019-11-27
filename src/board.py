from tkinter import *
from src.tile import Tile


ROW_SIZE = 5
COL_SIZE = 5


class Board:

    def __init__(self, master, num):
        self.id = num
        self.master = master
        self.boardFrame = Frame(self.master)
        self.boardFrame.config(highlightbackground="black", highlightthickness=2)

        self.tileSection = Frame(self.boardFrame)
        self.tileSection.config(highlightbackground="black", highlightthickness=1)

        self.tiles = []
        self.hasBingo = False

        self.fillHeader()
        self.fillBoard()


    def hasBingo(self):
        return self.hasBingo


    def updateTiles(self, tileVal):
        for r in range(ROW_SIZE):
            for c in range(COL_SIZE):
                if self.tiles[r][c].getValue() == tileVal:
                    pass # TODO finish this method, then the random generator one

    def render(self):
        self.boardFrame.place(relx=0.5, rely=0.2, anchor=N)


    def focus(self):
        self.boardFrame.lift()


    def fillHeader(self):
        self.title = Label(self.boardFrame, text="Board #%d" % self.id, borderwidth=1)
        #self.title.config(relief="solid", borderwidth=1)

        self.title.config(font=("Helvetica", 26))
        self.title.pack()


    def fillBoard(self):
        for r in range(ROW_SIZE):
            tilerow = []
            for c in range(COL_SIZE):
                tilerow.append(Tile(self.tileSection, "%s%s" % (r, c), r, c))
            self.tiles.append(tilerow)

        self.tileSection.pack()
