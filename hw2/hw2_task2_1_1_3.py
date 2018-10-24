from string import ascii_letters

# print letters, that are in ascii_letters, and how many times they appear in file

file_name = 'text_file.txt'

with open(file_name, 'r') as f:
    text = f.read()

chars_dict = {}
for i in text:
    if i in chars_dict.keys():
        chars_dict[i] += 1
    else:
        chars_dict[i] = 1

for key, value in chars_dict.items():
    if key in ascii_letters:
        print("Symbol: {}, appeared in text: {} times.".format(key, value))
