from re import fullmatch

reg_exp_pattern = '[+\-]?\d+(\.\d+)?'

positive = ['1', '-23', '456.789', '0']
negative = ['hello!']

for i in positive + negative:
    match = fullmatch(reg_exp_pattern, i)
    if match:
        print(i, " - matched")
    else:
        print(i, " - not matched")
