from re import fullmatch

reg_exp_pattern = '.o+.{2}'

positive = ['rock', 'core', 'roar', 'doors', 'looolz']
negative = ['hog', 'rack', 'shock', 'pocket']

for i in positive + negative:
    match = fullmatch(reg_exp_pattern, i)
    if match:
        print(i, " - matched")
    else:
        print(i, " - not matched")
