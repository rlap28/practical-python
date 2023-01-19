# tableformat.py

class FormatError(Exception):
    pass

class TableFormatter:
	def headings(self, headers):
		'''
		Emit the table headings
		'''
		raise NotImplementedError()

	def row(self, rowdata):
		'''
		Emit a single row of table data
		'''
		raise NotImplementedError()

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    '''
    Output portfolio data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
        	print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
        	print(f'<td>{d}</td>', end='')
        print('</tr>')

def create_formatter(name):
	'''
	Create TableFormatter object depending on desired output data format
	'''
	if name == 'txt':
		formatter = TextTableFormatter()
	elif name == 'csv':
		formatter = CSVTableFormatter()
	elif name == 'html':
		formatter = HTMLTableFormatter()
	else:
		raise FormatError('Unknown table format %s' % name)

	return formatter

def print_table(reportdata, columns, formatter):
	'''
	Print only [columns] of reportdata in deisred output data format
	'''
	formatter.headings(columns)
	for report in reportdata:
		rowdata = [str(getattr(report, column)) for column in columns]
		formatter.row(rowdata)




