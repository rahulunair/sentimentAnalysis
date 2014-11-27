from time import sleep
import tweetTrek

__author__ = 'rahul'

from Tkinter import *
from ttk import *
import tkFont
import Tkinter as tk



# constants

SEARCH_BOX = "Enter any word"
TEXT = " Start the Analysis "
SCORE = " Sentiment score : "
SEARCH_BTN = " Search "
TEXT_TO_PRINT =  "0.96"
STATUS = "Downloading Tweets Now.."



class Gui():
    '''
    A class which will act as the graphical user interface to the sentiment analysis.
    author: rahul
    '''
    def progressbar(self):
        # progress bar
        self.progressbar = Progressbar(self.mainFrame, orient='horizontal', mode='indeterminate')
        self.progressbar.start(30)
        self.progressbar.grid(row=8, column=1,sticky=(S, E))

    def kill_progressbar(self):
        self.progressbar.step()
        self.progressbar.stop()


    def reset_progressbar(self):
        self.progressbar.step()



    def runApp(self):
        #print TEXT_TO_PRINT
        trekker = tweetTrek.TweetTrek("self.query")
        trekker.trek()
        self.progressbar()
        self.text1.insert(0, TEXT_TO_PRINT)
        self.text1.configure(state='readonly')
        #return TEXT_TO_PRINT

    def __init__(self, root):
        self.LOGO = PhotoImage(file="./res/images/emotions.gif")
        self.root = root
        self.root.title("Sentiment Analyzer")
        self.root.maxsize(width=380, height=500)
        self.font = tkFont.Font(family="Helvetica", size=30, weight=tkFont.BOLD)

    def callback(self, focus):
        '''
        callback to clear the text box once focus is on it.
        :param focus: self and focus
        :return: null
        '''
        self.query_entry.delete(0, END)
        self.query_entry.config(foreground="black")

    def create_entry(self):
        self.font = tkFont.Font(family="Helvetica", size=8)
        entry = tk.Entry(self.mainFrame)
        entry.config(font=self.font)

    def createView(self):
        '''
        Creates the main window, the textbox to enter search query and the search button.
        :return: none
        '''

        # Main page
        #self.mainFrame = Frame(self.root, padding="3 3 12 12")
        self.mainFrame = tk.Frame(self.root,width = "10")
        self.mainFrame.grid(column=1, row=0, sticky=(N, W, E, S), padx=5, pady=10)
        self.mainFrame.columnconfigure(5, weight=1)
        self.mainFrame.rowconfigure(5, weight=1)
        self.mainFrame.config(background = "#54727B")


        # heading
        self.query_text = Label(self.mainFrame, text=TEXT)
        self.query_text.config(font = self.font, foreground="#54727B")
        self.query_text.grid(row=0, column = 1)

        #Logo
        self.logo = Label(self.mainFrame, image=self.LOGO)
        self.logo.grid(row=1, column=1)


        # Search  box
       # self.query = StringVar()
        self.query_entry = MaxLengthEntry(self.mainFrame, maxlength=15)
        self.query_entry.grid(row=2, column=1)
        self.query = self.query_entry.get()



        self.query_entry.config(foreground="grey")
        self.query_entry.bind("<FocusIn>", self.callback)


        # Button to submit the query
        buttonfont = tkFont.Font(family="Helvetica")
        self.search_btn = Button(self.mainFrame, text=SEARCH_BTN, width=10, command=self.runApp)
        #self.search_btn['font'] = [buttonfont]
        self.search_btn.grid(row=3, column=1)

         # space
        self.text_label = Label(self.mainFrame, background="#54727B")
        self.text_label.grid(row=4, column=1)

        # label 2
        self.text_label = Label(self.mainFrame, text = SCORE, foreground="#54727B")
        self.text_label.config(font = self.font)
        self.text_label.grid(row=5, column=1)

        # text field to show the score
        self.text1 = tk.Entry(self.mainFrame, width=4,  foreground="BLUE")
        self.font = tkFont.Font(family="Helvetica", size=25)
        self.text1.config(font = self.font, state= 'normal')
        #self.text1.configure(state='readonly')
        self.text1.grid(row=6, column=1)

        # space
        self.text_label = Label(self.mainFrame, background="#54727B")
        self.text_label.grid(row=7, column=1)

        # status text
        self.text_label = Label(self.mainFrame,text = STATUS, background="#54727B")
        self.text_label.grid(row=8, column=1)

        #progressbar
        #self.progressbar()

        #kill progressbar
        #self.kill_progressbar()

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
