def compare_string_values(first_str, second_str):
    # можно было написать просто:
    # return second_string in first_string

    return second_string in first_string


first_string = input("Enter value for first string: ")
first_string = str(first_string)

second_string = input("Enter value for second string: ")
second_string = str(second_string)

if len(first_string) > 0 and len(second_string) > 0:
    if compare_string_values(first_string, second_string):
        print("Second string is a part of first string!")
    else:
        print("Second string is not a part of first string!")
else:
    print("Please enter not Null values")
