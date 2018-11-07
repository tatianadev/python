def find_min_value(input_values):
    min_value = min(input_values)
    return min_value


def find_max_value(input_values):
    max_value = max(input_values)
    return max_value


list_of_values = []

inserted_value = input("Enter value: ")

inserted_value = str(inserted_value)
for i in inserted_value:
    list_of_values.append(int(i))

result_min_value = find_min_value(list_of_values)
print("Min. value: %d" % result_min_value)

result_max_value = find_max_value(list_of_values)
print("Max. value: %d" % result_max_value)
