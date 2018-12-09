from re import fullmatch

reg_exp_pattern = '.ar'

positive = ['bar', 'car', 'far', 'war', '0ar', '$ar']
negative = ['bag', 'for', 'star', 'care']

for i in positive + negative:
    match = fullmatch(reg_exp_pattern, i)
    if match:
        print(i, " - matched")
    else:
        print(i, " - not matched")
