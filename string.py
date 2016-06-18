fruit = 'banana'
index = 0
while index < len(fruit):
	letter = fruit[index]
	print letter 
	index = index + 1 



## same as below 

for char in fruit:
	print char 

## next character in fruit is assigned to the variable char 



prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	print letter + suffix




## string slices 
fruit = 'mangoes'
fruit[0:3]
'man'
fruit[:]
'mangoes'



greeting = 'hello, world'
greeting[0] = 'J'
## string is immutable 

greeting2 = 'J' + greeting[1:]




def find(word, letter):
	index = 0
	while index < len(word):
		if word[index] == letter:
			return index 
		index = index + 1 
	return -1  



## find method can be used as below

fruit = 'strawberries'
word = fruit.find('s')




## first trial version 
def in_both(word1, word2):
	for w1 in word1:
		for w2 in word2:
			if w1 == w2:
				print w1 



## second version using 'in' keyword (by using if)
def in_both2(word1, word2):
	for w1 in word1:
		if w1 in word2:
			print w1




word = 'orange'

if word == 'orange':
	print 'orange is here'



if word < 'banana':
		print 'Your word ' + word + ', comes before banana'
elif word > 'banana':
		print 'Your word ' + word + ', comes after banana' 




def is_reverse(word1, word2):
	if not len(word1) == len(word2):
		return False
	i = 0
	j = len(word1) - 1
	while i < j:
		if not word1[i] == word2[j]:
			return False
		i = i + 1
		j = j - 1
	return True









