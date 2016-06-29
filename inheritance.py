# default card is the 1 of Clubs
class Poker(object):
	"""Represents a standard playing card """
	def __init__(self, suit=0, rank=1):
		self.suit = suit
		self.rank = rank
	
	suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
	rank_names = [None, 'Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
	
	def __str__(self):
		return '%s of %s' % (Poker.rank_names[self.rank], Poker.suit_names[self.suit]) 

	def __cmp__(self, other):
		if self.suit > other.suit: return 1
		if self.suit < other.suit: return -1
		if self.rank > other.rank: return 1 
		if self.rank < other.rank: return -1
		return 0
#__str__ is like a toString() in java

class Deck(object):
	def __init__(self):
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14): 
				card = Poker(suit, rank)
				self.cards.append(card)

	def __str__(self):
		res = []
		for cards in self.cards:
			res.append(str(cards))
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self, card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)

	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())
			

class Player(Deck):
	"""Represents a deck in player's hands"""
	def __init__(self, label=''):
	self.cards = []
	self.label = label 


