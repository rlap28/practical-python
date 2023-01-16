# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            # holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_prices(filename):

    stock_prices = {}

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                stock_prices[row[0]] = float(row[1])
            except IndexError:
                pass

    return stock_prices

def gain_calc():
    portfolio = read_portfolio('Data/portfolio.csv')
    stock_prices = read_prices('Data/prices.csv')

    gain = 0.0
    for s in portfolio:
        gain += s['shares']*(stock_prices[s['name']]-s['price'])

    return gain

def make_report(portfolio, prices):

    report = []

    for s in portfolio:
        report.append((s['name'], s['shares'],
            prices[s['name']], prices[s['name']]-s['price']))

    headers = ('Name', 'Shares', 'Price', 'Change')
    for header in headers:
        print(f'{header:>10s}', end = ' ')

    print('')

    for header in headers:
        print('-'*10, end = ' ')

    print('')

    
    # for r in report:
    #     print('%10s %10d %10.2f %10.2f' % r)

    for name, shares, price, change in report:
        price_mod = '$' + str('%.2f' % price)
        print(f'{name:>10s} {shares:>10d} {price_mod:>10s} {change:>10.2f}')



