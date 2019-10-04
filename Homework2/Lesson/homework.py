from simpleeval import simple_eval
import math

def calculate_string(s):
        s = s.replace('pi', math.pi)
        s = s.replace('e', math.e)
        try:
            result = simple_eval(s)
        except Exception as e:
            return e
        else:
            return result
            
def calculate(s):
        try:
            s = simple_eval(s)
        except Exception :
            return 'Wrong input'
        else:
            return s
            
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