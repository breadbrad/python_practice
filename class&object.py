class Point(object):
		"""Represents a point 
			attributes: x, y """



class Rectangle(object):
		"""Represents a Rectangle
		attributes: width, height, corner"""

# >>> box = Rectangle()
# >>> box.width = 250.0
# >>> box.height = 500.0
# >>> box.corner = Point()
# >>> box.corner.x = 0.0
# >>> box.corner.y = 0.0

'''Copying '''

import copy 
y = copy.copy(x)
''' shallow copy
	x -> obj
		  ^
	      |
	      y
'''

# *********************** # 


z = copy.deepcopy(x)
''' deep copy
	obj obj
	 ^   ^
	 |   |
	 x 	 z
'''





