# pcost.py
#
# Exercise 1.27
import sys

def portfolio_cost(filename):
	'Evaluating total cost of shares portfolio'
	import csv
	total_cost = 0

	f = open(filename)
	rows = csv.reader(f)
	for row in rows:
		try:
			total_cost = total_cost + float(row[1]) * float(row[2])
		except ValueError:
			pass
	# with open(filename, 'rt') as f:
	# 	headers = next(f)
	# 	for line in f:
	# 		row = line.split(',')
	# 		try:
	# 			total_cost = total_cost + float(row[1]) * float(row[2])
	# 		except ValueError:
	# 			pass

	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)