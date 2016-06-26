import os 
## os represents operating system 
print os.getcwd() 
## current working directory 

def walk(directory):  
	for dirname in os.listdir(directory):
		path = os.path.join(directory, dirname)
	if os.path.isfile(path):
		print path
	else:
		walk(path)
# os.path.join takes a directory and a file name and joins them into a compelete path 


# catching exceptions 
try: 
	fin = open('file_name')
	for line in fin:
		print line 
	fin.close()
except:
	print 'Error..'

'''Database -> it's like a dictionary
	anydbm -> provides an interface for creating & updating db files ''' 

import anydbm
# c -> it creates if it doesn't exist 
db = anydbm.open('newfile.db', 'c')

'''Pickle ! -> translate any type of object into a string 
					(suitable for storage in a database'''

import pickle 
t = [1, 2, 3]
pickle.dumps(t)

# to interpret this, let's use pickle.loads("load string")

t2 = pickle.loads(t)
print t2 

'''Pipe -> an object the represents a running program '''

'''writing modules '''

import lc
# __name__ -> built-in variable (when the program starts)
# if the program is running as a script, __name__ has the value __main__
# if the module is being imported, the test code would be skipped 
if __name__ == '__main__':
		print linecount('lc.py')







