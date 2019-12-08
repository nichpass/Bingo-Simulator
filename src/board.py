from tkinter import *
from random import randint
from tile import Tile
from util import tileValues, Utility

ROW_SIZE = 5
COL_SIZE = 5


class Board:

    def __init__(self, master, num, tiles = None):
        self.id = num
        self.master = master
        self.bingoStatus = False
        self.boardFrame = Frame(self.master)

        self.fillHeader()

        self.boardFrame.config(highlightbackground="black", highlightthickness=2)
        self.tileSection = Frame(self.boardFrame)
        self.tileSection.config(highlightbackground="black", highlightthickness=1)

        self.tiles = []
        self.fillBoard()


    def getMaster(self):
        return self.master

    def hasBingo(self):
        return self.bingoStatus


    def checkBingo(self):
        # check horizontal cases
        for r in range(COL_SIZE):
            if all(tile.getSelectionVal() for tile in self.tiles[r]):
                print('found winner in horizontal of board #' + str(self.id))
                self.bingoStatus = True
                return True

        # check vertical cases
        for c in range(ROW_SIZE):
            column = []
            for r in range(COL_SIZE):
                column.append(self.tiles[r][c])
                # print("column contains: " + str(r) + ", " + str(c))
            if all(tile.getSelectionVal() for tile in column):
                print('found winner in vertical of board #' + str(self.id))
                self.bingoStatus = True
                return True

        # check the two diagonal cases
        leftCheck = True
        rightCheck = True

        for r in range(ROW_SIZE):
            for c in range(COL_SIZE):
                # check top-left to bottom-right diagonal
                if r == c and not self.tiles[r][c].getSelectionVal():
                    leftCheck = False

                # check bottom-left to top-right diagonal
                if (r + c) == 4 and not self.tiles[r][c].getSelectionVal():
                    rightCheck = False

        if leftCheck or rightCheck:
            print("found winner in diagonal of board #" + str(self.id))
            self.bingoStatus = True
        return self.bingoStatus

    def updateTiles(self, tileVal):

        for r in range(ROW_SIZE):
            for c in range(COL_SIZE):
                if self.tiles[r][c].getValue() == tileVal:
                    # print("updating tile: " + self.tiles[r][c].getValue())
                    self.tiles[r][c].setSelected()
                    self.tiles[r][c].getLabel().config(bg='red')

        self.checkBingo()


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
        tileVals = tileValues[:]
        for r in range(ROW_SIZE):
            tilerow = []
            for c in range(COL_SIZE):
                index = randint(0, len(tileVals)-1)
                tilerow.append(Tile(self.tileSection, tileVals[index], r, c))
                tileVals.pop(index)
            self.tiles.append(tilerow)

        self.tileSection.pack()

    def getId(self):
        return self.id

    def getTiles(self):
        return self.tiles