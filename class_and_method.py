# printing objects 
# to make function a method, move the function definition insdie the class 
class Time(object):
	"""Time class"""

start = Time()
start.hour = 9
start.minute = 45
start.second = 00




class Time(object):
	def print_time (time):
		print '%.2d:%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second)

Time.print_time(start)

## more concise 
start.print_time()

def is_after_(self, other):
	return 

'''__init__ is like a constructor in java'''

#inside class date:
def __init__ (self, day=1, month=1, year=2016):
	self.day = day
	self.month = month
	self.year = year 



