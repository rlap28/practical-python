# report.py
#
# Exercise 2.4

import sys
import csv
import fileparse as fp
import stock
import tableformat

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    
    with open(filename) as lines:
        portdicts = fp.parse_csv(lines, select = ['name', 'shares', 'price'],
            types = [str, int, float])

    portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]
    return portfolio

def read_prices(filename):

    with open(filename) as lines:
        return dict(fp.parse_csv(lines, types = [str, float],
            has_headers = False))

# def read_portfolio(filename):
#     '''Computes the total cost (shares*price) of a portfolio file'''
#     portfolio = []

#     # with open(filename, 'rt') as f:
#     #     rows = csv.reader(f)
#     #     headers = next(rows)
#     #     for row in rows:
#     #         holding = dict(zip(headers, row))
#     #         portfolio.append(holding)
#     # return portfolio

#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         headers = next(rows)
#         for row in rows:
#             holding = {}
#             holding['name'] = row[0]
#             holding['shares'] = int(row[1])
#             holding['price'] = float(row[2])
#             # holding = (row[0], int(row[1]), float(row[2]))
#             portfolio.append(holding)
#     return portfolio

# def read_prices(filename):

#     stock_prices = {}

#     with open(filename, 'rt') as f:
#         rows = csv.reader(f)
#         for row in rows:
#             try:
#                 stock_prices[row[0]] = float(row[1])
#             except IndexError:
#                 pass

#     return stock_prices

def gain_calc():
    portfolio = read_portfolio('Data/portfolio.csv')
    stock_prices = read_prices('Data/prices.csv')

    gain = 0.0
    for s in portfolio:
        gain += s['shares']*(stock_prices[s['name']]-s['price'])

    return gain

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name','Shares','Price','Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price data files.
    '''    
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)

    report = []

    for s in portfolio:
        report.append((s.name, s.shares,
            prices[s.name], prices[s.name]-s.price))

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

# def print_report(reportdata):
#     '''
#     Print a nicely formatted table from a list of (name, shares, price, change) tuples.
#     '''
#     headers = ('Name', 'Shares', 'Price', 'Change')
#     print('%10s %10s %10s %10s'  % headers)
#     print(('-' * 10 + ' ') * len(headers))
#     for row in reportdata:
#         print('%10s %10d %10.2f %10.2f' % row)

# def portfolio_report(portfolio_filename, prices_filename):

#     portfolio = read_portfolio(portfolio_filename)
#     prices = read_prices(prices_filename)

#     report = []

#     for s in portfolio:
#         report.append((s.name, s.shares,
#             prices[s.name], prices[s.name]-s.price))

#     print_report(report)

def main(argv):
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':    
    main(sys.argv)



