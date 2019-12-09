from tkinter import Label

class Tile:

    def __init__(self, master, value, r, c):
        self.master = master
        self.value = value
        self.isSelected = False

        self.label = Label(self.master, text=value, borderwidth=1)
        self.label.config(font=("Helvetica", 16))
        self.label.config(width=4, height=2)
        self.label.config(relief="solid", borderwidth=1)
        self.label.grid(row=r, column=c)

    def setSelected(self):
        self.isSelected = True

    def getSelectionVal(self):
        return self.isSelected

    def getLabel(self):
        return self.label

    def getValue(self):
        return self.value