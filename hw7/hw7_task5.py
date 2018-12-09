from re import sub

text_str = "The dog trotted forward with a short, sharp bark, and the keeper lifted his face suddenly and saw her."

reg_exp_pattern = '((^(The|A)\s)|\s(the|a)\s)'
change_str = ' '

result = sub(reg_exp_pattern, change_str, text_str)
print(text_str)
print(result)
