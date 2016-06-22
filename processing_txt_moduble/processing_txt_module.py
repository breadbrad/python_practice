import string
def process_file(filename):
	hist = dict()
	fp = open(filename)
	for line in fp:
		process_line(line, hist)
	return hist

def process_line(line, hist):
	line = line.replace('-', ' ')
	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace)
		word = word.lower()
		hist[word] = hist.get(word, 0) + 1


def total_words(hist):
	return sum(hist.values())
		
# the number of different words = the number of items in the dictionary 
# https://www.google.com/search?q=dictionary+python&espv=2&biw=1422&bih=788&source=lnms&tbm=isch&sa=X&ved=0ahUKEwj4zoCmzLrNAhUG02MKHfNkCwIQ_AUIDCgA#imgrc=Oou1T6qNr0KLCM%3A

def different_words(hist):
	return len(hist)
# DSU pattern - decorate, sort, undecorate 
# http://cs.colgate.edu/~efourquet/cosc101/c/h29.pdf
'''
Decorate - Make a list of pairs where the first item in the pair is the value by which you want to
sort and the second item is the data you want sorted
Sort - Sort the list 
Undecorate - Extract the desired data from the list.
'''

hist = process_file('emma.txt')

def most_common(hist):
	t = []
	for key, value in hist.items():
		t.append((value, key))
	t.sort(reverse=True)	
	return t

for freq, word in t[0:10]:
	print word, '\t', freq


def random_word(h):
	t = []
	for word, freq in h.items():
		t.extend([word] * freq)

## expression [word] * freq -> creates a list with freq copies of the string word 
## extend method -> the argument is a sequence 















