import os
from sys import argv
from dictionary import Dictionary

word = argv[1]

database = Dictionary()
file_name = 'list.txt'
directory = 'data'
file = os.path.join(os.getcwd(), directory, file_name)

# Build the database
with open(file=file, mode='r') as f:
    # Get rid of the first line, it's empty
    line = f.readline().rstrip()
    # Store the data
    while (line := f.readline()):
        if not line:
            continue
        line = line.strip()
        database.append(line.lower())

print(database[word])
