from string import ascii_letters

# print letters, that are in ascii_letters, and how many times they appear in file

file_name = 'text_file.txt'

with open(file_name, 'r') as f:
    data_from_file = f.read()

new_dict = {}
for symbol in data_from_file:
    if symbol in new_dict.keys():
        new_dict[symbol] += 1
    else:
        new_dict[symbol] = 1

for key, value in new_dict.items():
    if key in ascii_letters:
        print("Symbol: {}, appeared in text: {} times.".format(ascii(key), value))
