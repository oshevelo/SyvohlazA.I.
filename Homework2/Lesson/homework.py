from simpleeval import simple_eval

def calculate_string(s):
        try:
           s = simple_eval(s)
        except Exception:
           return 'Wrong input'
        else:
            return s

def calculate(s):
    s = str(s)
    if s.isdigit():
        return float(s)
    for c in ('-', '+', '*', '/'):
        right, op, left = s.partition(c)
        if op == '*':
            return calculate(left) * calculate(right)
        elif op == '/':
            return calculate(left) / calculate(right)
        elif op == '+':
            return calculate(left) + calculate(right)
        elif op == '-':
            return calculate(left) - calculate(right)

def calculator(operand1, operand2, operation='+'):
    try:
        operand1, operand2 = float(operand1), float(operand2)
    except ValueError:
        return 'Input error: value must be float numbers'
    else:
        if operation == '+':
            print('result =', operand1 + operand2)
        elif operation == '-':
            print('result =', operand1 - operand2)
        elif operation == '*':
            print('result =', operand1 * operand2)
        elif operation == '**':
            print('result =', operand1 ** operand2)
        elif operation == '/':
            if operand2 == 0:
                return 'Division by zero'
            else:
                print('result =', operand1 / operand2)
        else:
            print('Wrong symbol operation')