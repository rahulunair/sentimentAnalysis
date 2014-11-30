import DynamicGraph
import analysis

__author__ = 'rahul'

from Tkinter import *
from ttk import *
import tkFont
import Tkinter as tk
import threading
from time import sleep
from analysis import score_them
import parseTweets
import tweetTrek


# constants

SEARCH_BOX = "Enter any word"
TEXT = " Start the Analysis "
SCORE = " Sentiment score : "
SEARCH_BTN = " Search "
TEXT_TO_PRINT = "0.96"
STATUS = " "


class Gui():
    '''
    A class which will act as the graphical user interface to the sentiment analysis application.
    author: rahul
    '''

    def __init__(self, root):
        self.LOGO = PhotoImage(file="./res/images/emotions.gif")
        self.root = root
        self.root.title("Sentiment Analyzer")
        self.root.maxsize(width=380, height=500)
        self.font = tkFont.Font(family="Helvetica", size=30, weight=tkFont.BOLD)

    def sweep_tw(self):
        '''
        calls the trek() method of TweetTrek class
        :return: none
        '''
        trekker = tweetTrek.TweetTrek(self.query_entry.get())
        self.status_1 = trekker.trek()

    def tokenize(self):
        '''
        parse and split the tweets into tweet text and tweet id
        :return:
        '''
        parser = parseTweets.ParseTweets("tweets.json")
        parser.parse()


    def repaint(self, stat):
        '''
        Reload the graphical user interface with the progressbar and all other widgets when called
        :param stat:
        :return:
        '''

        print "entered text: ", self.query_entry.get()
        # status text
        STATUS = stat
        self.text_label = Label(self.mainFrame, text=STATUS, background="#54727B")
        self.text_label.grid(row=8, column=1)
        self.pBar = Progressbar(self.mainFrame, orient='horizontal', mode='determinate')
        self.pBar.grid(row=8, column=1, sticky=(S, E))
        self.pBar.start(50)
        self.pBar.update_idletasks()
        self.status_1 = 0


    def runApp(self):
        '''
        The main method of the application, called when search button is pressed, the action is here!!.
        '''
        t_0 = threading.Thread(target=self.repaint("Downloading Tweets Now.."))
        # self.repaint()
        t_1 = threading.Thread(target=self.sweep_tw())
        t_2 = threading.Thread(target=self.tokenize())
        t_0.start()
        t_1.start()
        while not t_1.isAlive():
            self.repaint("  Parsing and Tokenizing   ")
            self.pBar.update_idletasks()
            t_2.start()
            break
        sleep(7)
        self.repaint("  Chanting the magic spell...   ")
        self.pBar.update_idletasks()
        sentiment = score_them()
        #analysis.dyna_g.on_close()
        self.text1.configure(state='normal')
        self.text1.delete(0, END)
        self.text1.insert(0, round(sentiment, 2))
        self.text1.configure(state='readonly')
        sleep(7)
        self.repaint("            Finished                ")
        self.pBar.update_idletasks()
        self.pBar.stop()
        #print sentiment


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
        # self.mainFrame = Frame(self.root, padding="3 3 12 12")
        self.mainFrame = tk.Frame(self.root, width="10")
        self.mainFrame.grid(column=1, row=0, sticky=(N, W, E, S), padx=5, pady=10)
        self.mainFrame.columnconfigure(5, weight=1)
        self.mainFrame.rowconfigure(5, weight=1)
        self.mainFrame.config(background="#54727B")



        # heading
        self.query_text = Label(self.mainFrame, text=TEXT)
        self.query_text.config(font=self.font, foreground="#54727B")
        self.query_text.grid(row=0, column=1)

        #Logo
        self.logo = Label(self.mainFrame, image=self.LOGO)
        self.logo.grid(row=1, column=1)


        # Search  box
        self.query = StringVar()
        self.query_entry = MaxLengthEntry(self.mainFrame,
                                          maxlength=20)  # limited the length of word that can be entered to 20
        self.query_entry.grid(row=2, column=1)
        print   "query_entry is: ", self.query_entry.get()

        self.query_entry.config(foreground="grey")
        i = 0
        if i == 0:
            self.query_entry.bind("<FocusIn>", self.callback)
            i = 1


        # Button to submit the query
        self.search_btn = Button(self.mainFrame, text=SEARCH_BTN, width=10, command=self.runApp)
        self.search_btn.grid(row=3, column=1)

        # space
        self.text_label = Label(self.mainFrame, background="#54727B")
        self.text_label.grid(row=4, column=1)

        # label 2
        self.text_label = Label(self.mainFrame, text=SCORE, foreground="#54727B")
        self.text_label.config(font=self.font)
        self.text_label.grid(row=5, column=1)

        # text field to show the score
        self.text1 = tk.Entry(self.mainFrame, width=4, foreground="BLUE")
        self.font = tkFont.Font(family="Helvetica", size=25)
        self.text1.config(font=self.font, state='normal')
        self.text1.grid(row=6, column=1)

        # space
        self.text_label = Label(self.mainFrame, background="#54727B")
        self.text_label.grid(row=7, column=1)

        for child in self.mainFrame.winfo_children(): child.grid_configure(padx=5, pady=5)


class ValidatingEntry(Entry):
    # base class for validating entry widgets



    def __init__(self, master, value="", **kw):
        self.font = tkFont.Font(family="Helvetica", size=14)
        apply(Entry.__init__, (self, master), kw)
        self.__value = value
        self.__variable = StringVar()
        self.__variable.set(SEARCH_BOX)
        self.config(font=self.font)
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
        return value


class MaxLengthEntry(ValidatingEntry):
    '''
    class which limits the length of the word entered into the search column
    '''

    def __init__(self, master, value="", maxlength=None, **kw):
        self.maxlength = maxlength
        apply(ValidatingEntry.__init__, (self, master), kw)

    def validate(self, value):
        if self.maxlength is None or len(value) <= self.maxlength:
            return value
        return None  # new value too long

# method call to run the app

if __name__ == '__main__':
    root = Toplevel()
    gui = Gui(root)
    gui.createView()
    root.mainloop()
