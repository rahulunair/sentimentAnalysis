__author__ = 'rahul'

from Tkinter import *
from ttk import *
import tkFont
import Tkinter as tk



# constants

SEARCH_BOX = "Enter any word"
TEXT = "Enter a Word to Start the Analysis: "
SEARCH_BTN = "Search"


def runApp():
    print "hello world"

class Gui():
    '''
    A class which will act as the graphical user interface to the sentiment analysis.
    author: rahul
    '''

    def __init__(self, root):
        self.LOGO = PhotoImage(file="./res/images/emotions.gif")
        self.root = root
        self.root.title("Sentiment Analyzer")
        self.root.maxsize(width=596, height=600)
        self.font = tkFont.Font(family="Helvetica", size=20, weight=tkFont.BOLD)

    def callback(self, focus):
        '''
        callback to clear the text box once focus is on it.
        :param focus: self and focus
        :return: null
        '''
        self.query_entry.delete(0, END)
        self.query_entry.config(foreground="black")

    def createView(self):
        '''
        Creates the main window, the textbox to enter search query and the search button.
        :return: none
        '''

        # Main page
        #self.mainFrame = Frame(self.root, padding="3 3 12 12")
        self.mainFrame = tk.Frame(self.root)
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=30)
        self.mainFrame.columnconfigure(0, weight=1)
        self.mainFrame.rowconfigure(0, weight=1)
        self.mainFrame.config(background = "#54727B")

        #Logo
        self.logo = Label(root, image=self.LOGO)
        self.logo.grid(row=0, column=1)

        # Query text formatting
        self.query_text = Label(self.mainFrame, text=TEXT)
        self.query_text.config(font = self.font)
        #self.query_text.grid(row=1, column=0, sticky=(N, W))

        # Text box
        self.query = StringVar()
        self.query_entry = MaxLengthEntry(self.mainFrame, maxlength=15)
        #self.query_entry.grid(row=1, column=1, sticky=(W, E))

        self.query_entry.config(foreground="grey")
        self.query_entry.bind("<FocusIn>", self.callback)

        # Button to submit the query
        buttonfont = tkFont.Font(family="Helvetica")
        self.search_btn = Button(self.mainFrame, text=SEARCH_BTN, width=10, command=runApp)
        #self.search_btn['font'] = [buttonfont]
        #self.search_btn.grid(row=1, column=2)

        for child in self.mainFrame.winfo_children(): child.grid_configure(padx=5, pady=5)


class ValidatingEntry(Entry):
    # base class for validating entry widgets



    def __init__(self, master, value="", **kw):
        self.font = tkFont.Font(family="Helvetica", size=14)
        apply(Entry.__init__, (self, master), kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(SEARCH_BOX)
        self.config(font = self.font)
        self.__variable.trace("w", self.__callback)
        self.config(textvariable=self.__variable)

    def __callback(self, *dummy):
        value = self.__variable.get()
        newvalue = self.validate(value)
        if newvalue is None:
            self.__variable.set(self.__value)
        elif newvalue != value:
            self.__value = newvalue
            self.__variable.set(self.newvalue)
        else:
            self.__value = value

    def validate(self, value):
        # override: return value, new value, or None if invalid
        return value


class MaxLengthEntry(ValidatingEntry):
    def __init__(self, master, value="", maxlength=None, **kw):
        self.maxlength = maxlength
        apply(ValidatingEntry.__init__, (self, master), kw)

    def validate(self, value):
        if self.maxlength is None or len(value) <= self.maxlength:
            return value
        return None  # new value too long


root = Tk()
gui = Gui(root)
gui.createView()
root.mainloop()