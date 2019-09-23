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


operand1 = input('Enter operand1: ')
operation = input('Enter operation: ')
operand2 = input('Enter operand2: ')

result = calculator(operand1=operand1,
                    operand2=operand2, operation=operation)

if isinstance(result, str):
    print(result)
