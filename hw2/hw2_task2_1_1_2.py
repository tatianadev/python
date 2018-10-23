file_name = 'text_file.txt'

total_number_of_words = 0
number_of_words_in_line = 0

with open(file_name, 'r') as f:
    for line in f:
        number_of_words_in_line = len(line.split())
        total_number_of_words += number_of_words_in_line

print("Number of words: %d" % total_number_of_words)
