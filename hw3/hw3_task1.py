import random
from functools import reduce

min_val = 1
max_val = 10
numbers = []


# first part of functions (for reduce)
def sum(x, y):
    return x + y


def multiply(x, y):
    return x * y


def join(x, y):
    return x * 10 + y


def union(x, y):
    x.add(y)
    return x


def reverse(x, y):
    x.insert(0, y)
    return x


# second part of functions (for map)
def negated(x):
    return -x


def inverted(x):
    return 1 / x


def squared(x):
    return x ** 2


# third part of functions (for filter)
def odds(x):
    return x % 2 != 0


def evens(x):
    return x % 2 == 0


def simples(x):
    return x in {1, 2, 3, 5, 7}


dict_for_reduce = {"sum": sum, "multiply": multiply, "join": join, "union": union, "reverse": reverse}
dict_reduce_val = {"sum": 0, "multiply": 1, "join": 0, "union": set(), "reverse": list()}

dict_for_filter = {"odds": odds, "evens": evens, "simples": simples}
dict_for_map = {"negated": negated, "inverted": inverted, "squared": squared}

input_number = int(input("Please enter number: "))

for i in range(0, input_number):
    new_number = random.randrange(min_val, max_val)
    numbers.append(new_number)

print("Generated values: {}".format(numbers))

input_actions = input("Please enter actions: ")
action = input_actions.split()
print("Actions: {}".format(action))

filtered_values = list(filter(dict_for_filter[action[2]], numbers))
print("Filtered values ({}): {}".format(action[2], filtered_values))

map_values = list(map(dict_for_map[action[1]], filtered_values))
print("Values after map ({}): {}".format(action[1], map_values))

reduce_values = reduce(dict_for_reduce[action[0]], map_values, dict_reduce_val[action[0]])
print("Values after reduce ({}): {}".format(action[0], reduce_values))
