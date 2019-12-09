from tkinter import Label, Toplevel

class WinWindow():

    def __init__(self, winners, master=None):
        self.master = Toplevel(master)
        self.master.geometry("400x200")
        self.winnerString = ""
        for i in range(len(winners)):
            self.winnerString += "BOARD #%d is a winner YEAH!\n" % winners[i].getId()
        print(self.winnerString)
        self.message = Label(self.master, text=self.winnerString)
        self.message.config(font=("Helvetica", 16))
        self.message.pack()



