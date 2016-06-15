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

