file_name = 'text_file.txt'

words_count_in_line = 0
total_words_count = 0

with open(file_name, 'r') as f:
    for line in f:
        words_count_in_line = len(line.split())
        total_words_count += words_count_in_line

print("Number of words: %d" % total_words_count)