import tweetTrek

__author__ = 'rahul'

import matplotlib.pyplot as plt

plt.ion()

class DynamicGraph:

    min_x = 0
    max_x = tweetTrek.RANGE * tweetTrek.COUNT

    def __init__(self):
        self.xdata = 0
        self.ydata = 0
        self.figure, self.ax = plt.subplots()
        self.lines, = self.ax.plot([],[])
        #Autoscale on unknown axis and known lims on the other
        self.ax.set_autoscaley_on(True)
        self.ax.set_xlim(self.min_x, self.max_x)
        #Other stuff
        self.ax.grid()


    def on_running(self, xdata, ydata):

        '''update the graph dynamically on the fly'''
        self.xdata = xdata
        self.ydata = ydata
        self.lines.set_xdata(self.xdata)
        self.lines.set_ydata(self.ydata)
        self.ax.relim()
        self.ax.autoscale_view()
        #We need to draw *and* flush
        self.figure.canvas.draw()
        self.figure.canvas.flush_events()
