######################################################################################################################
# Name: Jacob Ryans
# Date: 4/5/17
# Description: Sierpinski Triangle fractal program. Plots points linking together 
######################################################################################################################

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

    def midpoint(self, other):
        # Takes the x, y values of the first object and finds the x, y values of the inputted point and gets the midpt
        mp = Point((self.x + other.x)/2, (self.y + other.y)/2)
        return mp

    # Plots points and changes the point to red
    def redPt(self):
        #setting x and y to self.x and self.y (personal preference)
        x = self.x
        y = self.y
        #plots points with values set by you Mr. Anky-Sama
        s.create_oval(x,y, x+ POINT_RADIUS, y+ POINT_RADIUS, fill = POINT1_COLOR)

    # Plots points and changes the point to red
    def grePt(self):
        #setting x and y to self.x and self.y (personal preference)
        x = self.x
        y = self.y
        #plots points with values set by you Mr. Anky-Sama
        s.create_oval(x,y, x+ POINT_RADIUS, y+ POINT_RADIUS, fill = POINT2_COLOR)

    # Plots points and changes the point to red
    def bluPt(self):
        #setting x and y to self.x and self.y (personal preference)
        x = self.x
        y = self.y
        #plots points with values set by you Mr. Anky-Sama
        s.create_oval(x,y, x+ POINT_RADIUS, y+ POINT_RADIUS, fill = POINT3_COLOR)

    # Plots points normally
    def normPt(self):
        #setting x and y to self.x and self.y (personal preference)
        x = self.x
        y = self.y
        #plots points with values set by you Mr. Anky-Sama
        s.create_oval(x,y, x+ POINT_RADIUS, y+ POINT_RADIUS, fill = POINT_COLOR)

    # Plots vertex and changes the point to red
    def vertPt(self):
        #setting x and y to self.x and self.y (personal preference)
        x = self.x
        y = self.y
        #plots points with values set by you
        s.create_oval(x,y, x+ VERTEX_RADIUS, y+ VERTEX_RADIUS, fill = VERTEX_COLOR)



# the chaos game class
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    def __init__(self, master):
        #the canvas is initialized and set to white bg color
        Canvas.__init__(self, master, bg = "white")
        self.Canvas = Canvas(master)
        #canvas is packed
        self.pack(fill = BOTH, expand = 1)

    def play(self, n):
        #plots the vertices and forms the outline for the triangle
        p1 = Point(0, HEIGHT)
        p2 = Point(WIDTH/2, 0)
        p3 = Point(WIDTH, HEIGHT)
        #first midpoint is instantiated
        m = p1.midpoint(p2)
        #plots the red vertices so you can see the differentiation
        p1.redPt()
        p2.redPt()
        p3.redPt()
        #first midpoint is plotted
        m.grePt()
        #uses a for loop with NUM_POINTS (n) that is passed thru to use recursion 50000 times
        for i in range(n):
            #uses randint to pick a random number that represents the first step of the next midpoint that will be plotted
            x = randint(1, 3)
            #checks if the randint is 3
            if (x == 3):
                #p is the new point that is going to be instatiated
                p = p1.midpoint(m)
                #p is plotted
                p.grePt()
                #m replaces p, thus readying the next step of making Sierpinski's Triangle
                m = p
                #these same steps occur in the other two if statements, slowly filling in the triangle
            elif (x == 2):
                p = p2.midpoint(m)
                p.redPt()
                m = p
            elif (x == 1):
                p = p3.midpoint(m)
                p.bluPt()
                m = p
                
                    
                    
##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520
# the default vertex radius is 2 pixels and color is red
VERTEX_RADIUS = 2
VERTEX_COLOR = "red"
# the default point radius is 0 pixels and color is black
POINT_RADIUS = 0
POINT1_COLOR = "red"
POINT2_COLOR = "green"
POINT3_COLOR = "blue"
# the number of midpoints to plot
NUM_POINTS = 50000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the chaos game as a Tkinter canvas inside the window
s = ChaosGame(window)
# play the chaos game with at least 50000 points
s.play(NUM_POINTS)
# wait for the window to close
window.mainloop()
