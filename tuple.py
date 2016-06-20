# tuples 
addr = 'limd46@uwosh.edu'
id, domain = addr.split('@')


# the parameter that begins with * gathers argument into a tuple 

def printAstuple(*args):
	print args

# Exercise 12.1 
def sumall(*t):
	return sum(t)




# zip -> zips sequences into a list of tuples 

zip = ('POWER', '12345')

# directory[last, first] = number

#DSR  Decorate, Sort, Undecorate

def sort_by_length(words):
	t = [] 
	for word in words:
		t.append(len(word), word)
	t.sort(reverse=True)
	res = [] 
	for length, word in t:
		res.append(word)
	return res 

# when is tuple prefered?
# to be syntactically simpler (e.g. return statement)
# to use a sequence as a dictionary key (immutable)
# to pass a sequence as an argument to a function 