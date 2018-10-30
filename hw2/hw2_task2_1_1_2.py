file_name = 'text_file.txt'

total_words_count = 0

with open(file_name, 'r') as f:
    # то же, что и в предыдущей задаче - можно было сразу считать весь текст:
    # text = f.read()
    # total_words_count = len(text.split())

    text = f.read()
    total_words_count = len(text.split())

print("Number of words: %d" % total_words_count)
