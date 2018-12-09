from re import fullmatch

reg_exp_pattern = '(l|d)o(g|ck)'

positive = ['dog', 'log', 'dock', 'lock']
negative = ['fog', 'block', 'locked']

for i in positive + negative:
    match = fullmatch(reg_exp_pattern, i)
    if match:
        print(i, " - matched")
    else:
        print(i, " - not matched")
