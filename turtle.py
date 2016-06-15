from swampy.TurtleWorld import *
from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob 

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

def polygon(t, n, length):
	angle = 360.0 / n
	for i in range(n):
		fd(t, length)
		lt(t, angle)

import math 

def circle(t, r):
	circumference = 2 * math.pi * r
	n = 50 
	length = circumference / n
	polygon(t, n, length)

## refactoring -> rearrangingn a program to improve function interfaces
"""triple-quoted string --> for documentation 
"""
def polyline (t, n, length, angle):
	for i in range(n):
		fd(t, step_length)
		lt(t, step_angle)

def polygon(t, n, length):
	angle = 360.0 / n
	polyline(t, n, length, angle)

def arc(t, r, angle):
	arc_length = 2 * math.pi * r * angle
	n = int (arc_length / 3) + 1 
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_length, step_angle)

def circle(t, r):
	arc(t, r, 360)


try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *







