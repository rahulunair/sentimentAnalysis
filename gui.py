__author__ = 'rahul'

from Tkinter import *


def runApp():
    print "hello world"


class Gui():
    '''
    A class which will act as the graphical user interface to the sentiment analysis.
    author: rahul
    '''

    def __init__(self, root):
        self.root = root
        self.createView()
        self.root.title("Sentiment Analyzer")
        self.root.minsize(width = 300, height = 200)

    def createView(self):

        self.query_text = Label(self.root, text="Enter a word to start analsyis: ")
        self.query_text.grid(row=2, column=0)

        self.query_entry = Entry(self.root, bd=1)
        self.query_entry.grid(row=2, column=1)
        self.search_btn = Button(self.root, text="Submit", width=10, command=runApp)
        self.search_btn.grid(row=2, column=2)


root = Tk()
gui = Gui(root)
gui.createView()
root.mainloop()