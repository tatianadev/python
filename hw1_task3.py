def remove_zero_value(input_list):
    p = len(input_list) - 1  # position of last element in list

    while p >= 0:
        if input_list[p] == 0:
            del input_list[p]
        p -= 1

    return input_list


def generate_sieve_of_eratosthenes(input_list):
    k = 2
    t = 1
    while k < len(input_list):
        while t < len(input_list):
            if input_list[t] != 0 and input_list[t] != k and input_list[t] % k == 0:
                input_list[t] = 0
            t += 1
        k += 1
        t = k + 1

    final_result = remove_zero_value(input_list)
    print("Final result: {}".format(final_result))


list_of_values = []

input_value = input("Enter value: ")
input_value = int(input_value)
for i in range(1, input_value):  # add in list values from 1 to entered_value - 1
    list_of_values.append(i)

print("Original list of values: {}".format(list_of_values))

generate_sieve_of_eratosthenes(list_of_values)
