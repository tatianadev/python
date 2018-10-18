def check_palindrome(original_string):
    length_of_string = len(original_string)
    print("Original string: %s" % original_string)
    reverted_string = original_string[-1:-length_of_string - 1:-1]
    print("Reverted string: %s" % reverted_string)
    if original_string == reverted_string:
        print("This record is a palindrome!")
    else:
        print("This record is not a palindrome!")


input_string = input("Enter a string value: ")
input_string = str(input_string)
check_palindrome(input_string)