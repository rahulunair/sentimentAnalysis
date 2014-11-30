import numpy
import tweetTrek

__author__ = 'rahul'

import matplotlib.pyplot as plt

plt.ion()


class DynamicGraph:
    '''
    A class to draw sentiment of each tweet as a graph.
    '''

    min_x = 0
    max_x = tweetTrek.RANGE * tweetTrek.COUNT

    def __init__(self):
        self.xdata = 0
        self.ydata = 0
        self.figure, self.ax = plt.subplots()

        # self.lines, = self.ax.plot([],[], c=numpy.random.rand(3,1))
        #Autoscale on axis

        self.ax.set_autoscaley_on(True)
        self.ax.set_title("Sentiment Tracker")
        self.ax.set_xlabel("Number of tweets")
        self.ax.set_ylabel("Sentiment score")
        self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax.grid()


    def on_running(self, xdata, ydata):
        '''update the matplotlib dynamically on the fly with classified sentiment for each tweets'''

        print "Graphing started"
        self.xdata = xdata
        self.ydata = ydata
        lines, = self.ax.plot([], [], c='g')
        lines.set_xdata(self.xdata)
        lines.set_ydata(self.ydata)
        self.ax.relim()
        self.ax.autoscale_view()
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()

    def on_close(self):
        # plt.close(self.figure)
        plt.cla()