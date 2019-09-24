from simpleeval import simple_eval

def calculate_string(s):
    try:
       s = simple_eval(s)
    except Exception:
        return 'Wrong input'
    else:
        return s

s = input('Input expression: ')

print('result =', calculate_string(s))

