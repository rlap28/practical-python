from typedproperty import String, Integer, Float

class Stock:
	
	name = String('name')
	shares = Integer('shares')
	price = Float('price')

	def __init__(self, name, shares, price):
		'''
		Create new Stock object
		'''
		self.name = name
		self.shares = shares
		self.price = price

	def __repr__(self):
		return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

	@property
	def cost(self):
		'''
		Calculate the whole cost of Stock
		'''
		return self.shares * self.price

	def sell(self, num):
		'''
		Sell num amounts of shares of Stock
		'''
		self.shares -= num