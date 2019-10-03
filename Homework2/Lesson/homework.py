from simpleeval import simple_eval
def calculate_string(s):
        try:gs#bad syntax as for me
           s = simple_eval(s)
        except Exception:# as e
           return 'Wrong input'#'Wrong input {}'.format(e)
        else:
            return s

def calculate(s):
    s = str(s)#what for?
    if s.isdigit():
        '''
        #FIXME: 
        >>> s = '2.2'
        >>> s.isdigit()
        False
        >>> float(s)
        2.2
        '''
        return float(s)
    for c in ('-', '+', '*', '/'):
        left, op, right = s.partition(c)
        if op == '*':
            return calculate(left) * calculate(right)
        elif op == '/':
            return calculate(left) / calculate(right)
        elif op == '+':
            return calculate(left) + calculate(right)
        elif op == '-':
            return calculate(left) - calculate(right)
    '''
        >>> s = '2++2'
        >>> s.partition('+')
        ('2', '+', '+2')
        >>> left, op, right= s.partition('+')
        >>> right
        '+2'
        >>> right.partition('+')
        ('', '+', '2')
    '''

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
