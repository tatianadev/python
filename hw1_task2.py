def calculate_sum(input_value):
    sum_of_variables = 0
    for counter in range(1, input_value + 1):
        value_of_number = input("Input value for number %d: " % counter)
        value_of_number = int(value_of_number)
        if value_of_number % 3 == 0:
            sum_of_variables += value_of_number
    return sum_of_variables


number_of_variables = input("Input number of variables: ")
number_of_variables = int(number_of_variables)
result_sum = calculate_sum(number_of_variables)

print("Sum of values, that are divided by 3, in total: %d" % result_sum)
