import random

min_value = 1
max_value = 10

random_value = random.randint(min_value, max_value)

while True:
    # input value
    input_value = input("Enter value from 1 till 10: ")
    input_value = int(input_value)
    if input_value == random_value:
        print("You are right, random value is %d!" % random_value)
        break
    else:
        print("Try again!")
