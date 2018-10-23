file_name = 'text_file.txt'  # name of file

# notes:
# https://docs.python.org/3.7/tutorial/inputoutput.html#methods-of-file-objects
# f.read() reads the file as an individual string
# f.readline() reads a single line of the file
# Using the syntax for line in f: allows the user to iterate over the file line by line
# If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

# read data from file and print this data
with open(file_name, 'r') as f:
    for line in f:
        print(line, end='')
