class Stock:
	def __init__(self, name, shares, price):
		'''
		Create new Stock object
		'''
		self.name = name
		self.shares = shares
		self.price = price

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