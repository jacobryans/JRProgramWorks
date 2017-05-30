######################################################################################################################
# Name: Jacob Ryans
# Date: 3/27/17
# Description: Plots multi-colored points on a GUI 
######################################################################################################################
import math
from random import randint
from Tkinter import *

# the 2D point class
class Point(object):
    def __init__(self, x = 0.0, y = 0.0):
        self.y = float(y)
        self.x = float(x)

    # Setters and Getters to provide read/write access

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def midpt(self, other):
        # Takes the x, y values of the first object and finds the x, y values of the inputted point and gets the midpt
        return ((self.x + other.x)/2, (self.y + other.y)/2)

    def dist(self, other):
        # Takes the x, y values of the first object and finds the x, y values of the inputted point and gets the distance
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

        # Returns a string representation of the points
    def __str__(self):
        return "({},{})".format(self.x, self.y)

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg = "white")
        self.pack(fill = BOTH, expand = 1)

    def plotPoints(self, n):
        for i in range(n):
            x = randint(0,WIDTH-1)
            y = randint(0,HEIGHT-1)
            self.plot(x,y)
            
    def plot(self, x, y):
        color = COLORS[randint(0, len(COLORS)-1)]
        self.create_oval(x,y, x+ POINT_RADIUS, y+ POINT_RADIUS, outline = color, fill = color)  

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 400x400
WIDTH = 400
HEIGHT = 400
# the default point radius is 0 pixels (i.e., no center to the oval)
POINT_RADIUS = 0
# colors to choose from when plotting points
COLORS = [ "black", "red", "green", "blue", "cyan", "yellow", "magenta" ]
# the number of points to plot
NUM_POINTS = 100000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
