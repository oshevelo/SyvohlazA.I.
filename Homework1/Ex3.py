from simpleeval import simple_eval

def calculate_string(s):
    try:
       s = simple_eval(s)
    except Exception as e:
        return e
    else:
        return s
            
s = input('Input expression: ')

s = s.replace('pi', '3.14')
s = s.replace('e', '2.71')

print('result =', calculate_string(s))

