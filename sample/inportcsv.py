import csv
from collections import namedtuple

with open('sample/movies.csv', newline="") as infile:
    reader = csv.reader(infile)
    Data = namedtuple("Data", next(reader))  # get names from column headers
    for data in map(Data._make, reader):
        print(data.foo)
        # ...further processing of a line...