# pcost.py
#
# Exercise 1.27
import sys
import report as rep

def portfolio_cost(filename):
	'Evaluating total cost of shares portfolio'

	return sum([s.shares*s.price for s in rep.read_portfolio(filename)])

# def portfolio_cost(filename):
# 	'Evaluating total cost of shares portfolio'
# 	import csv
# 	total_cost = 0

# 	f = open(filename)
# 	rows = csv.reader(f)
# 	headers = next(rows)
# 	for rowno, row in enumerate(rows, start=1):
# 		record = dict(zip(headers, row))
# 		try:
# 			nshares = int(record['shares'])
# 			price = float(record['price'])
# 			total_cost += nshares * price
# 		except ValueError:
# 			print(f'Row {rowno}: Bad row: {row}')
# 	# for row in rows:
# 	# 	try:
# 	# 		total_cost = total_cost + float(row[1]) * float(row[2])
# 	# 	except ValueError:
# 	# 		pass
# 	# with open(filename, 'rt') as f:
# 	# 	headers = next(f)
# 	# 	for line in f:
# 	# 		row = line.split(',')
# 	# 		try:
# 	# 			total_cost = total_cost + float(row[1]) * float(row[2])
# 	# 		except ValueError:
# 	# 			pass

# 	return total_cost

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
	filename = 'Data/portfolio.csv'

def main(argv):
	print('Total cost:', portfolio_cost(argv[1]))

if __name__ == '__main__':
	main(sys.argv)

