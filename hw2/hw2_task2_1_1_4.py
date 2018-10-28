file_name = 'text_file.txt'
second_file = 'new_file.txt'
odd_numb_of_lines = False
EOL_symbol = '\n'

with open(file_name, 'r') as f:
    file_lines = f.read().splitlines()

numb_of_lines = len(file_lines)

if numb_of_lines % 2 != 0:
    odd_numb_of_lines = True
    middle_line_numb = int(numb_of_lines // 2 + 1)
else:
    middle_line_numb = int(numb_of_lines / 2)

# write into file
with open(second_file, 'w') as f:
    # write to file second part of lines
    for i in range(middle_line_numb, len(file_lines)):
        f.write(file_lines[i] + EOL_symbol)

    # write to file middle line, if number of lines is odd
    if odd_numb_of_lines:
        f.write(file_lines[middle_line_numb - 1] + EOL_symbol)
        middle_line_numb = middle_line_numb - 1

    # write to file first part of lines
    for i in range(0, middle_line_numb):
        f.write(file_lines[i] + EOL_symbol)