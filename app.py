import os
from sys import argv
from dictionary import Dictionary
import os

word = argv[1]
database = Dictionary()
file_name = 'list.txt'
file = os.path.join(os.getcwd(), file_name)

with open(file=file, mode='r') as f:
    # Get rid of the first line, it's empty
    line = f.readline().rstrip()
    # Store the data
    while (line := f.readline().rstrip()):
        if line != "":
            database.append(line)

print(database[word])
