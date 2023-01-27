# fileparse.py
#
# Exercise 3.3

import csv
import logging
log = logging.getLogger(__name__)

def parse_csv(lines, select = None, types = None, has_headers = True,
    delimiter = ',', silence_errors = False):
    '''
    Parse a CSV file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    rows = csv.reader(lines, delimiter = delimiter)

    # Read the file headers
    headers = next(rows) if has_headers else []

    # Choose the user-specified columns
    if select:
        indices = [headers.index(column) for column in select]
    else:
        indices = []

    records = []
    for rowno, row in enumerate(rows, 1):
        if not row:    # Skip rows with no data
            continue
        if indices:
            row = [row[index] for index in indices]
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    log.warning("Row %d: Couldn't convert %s", rowno, row)
                    log.debug("Row %d: Reason %s", rowno, e)
                continue

        if headers:
            # Create dictionary and append list
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)

    return records