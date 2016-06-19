## dictionaries like a map (key, value)
## can be searched by its key value 
## in order to use values 
vals = eng2sp.values()



## set of counters 

def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d 



def print_hist(h):
	for c in h:
		print c, h[c]




def reverse_lookup(d, v):
	res = [] 
	for k in d:
			if d[k] == v:
				res.append(k)
	return res
	raise ValueError 



def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

## dictionary is implemented using a hashtable and the keys have to be hashable 

## dictionaries are mutable -> NO for keys , YES for values 


## memoization ##

known = {0:0, 1:1}

## fibonacci memoization version 
## it uses result that is already there 

def fibonacci(n):
	if n in known:
		return known[n]
	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res 

































