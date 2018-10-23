file_name = 'text_file.txt'
second_file = 'new_file.txt'

with open(file_name, 'r') as f:
    records_from_file = f.readlines()

number_of_records = len(records_from_file)


if number_of_records % 2 != 0:
    number_of_middle_record = int(number_of_records // 2 + 1)
else:
    number_of_middle_record = int(number_of_records / 2)

counter = number_of_middle_record

# write into file
with open(second_file, 'w') as f:
    # write to file second part of lines
    while counter < len(records_from_file):
        f.write(records_from_file[counter])
        counter += 1

    # write to file middle record, if number of records is odd
    if number_of_records % 2 != 0:
        f.write(records_from_file[number_of_middle_record - 1])
        number_of_middle_record = number_of_middle_record - 1

    # write to file first part of lines
    i = 0
    while i < number_of_middle_record:
        f.write(records_from_file[i])
        i += 1
