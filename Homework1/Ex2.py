'''
Данное решение готово, но не учитывает порядок операций,
но это будет доработано.
Третье задание пока в работе.
'''

def calculate(operand1, operand2, operation='+'):
    try:
        operand1, operand2 = float(operand1), float(operand2)
    except ValueError:
        return 'Input error'
    else:
        if operation == '+':
            return operand1 + operand2
        elif operation == '-':
            return operand1 - operand2
        elif operation == '*':
            return operand1 * operand2
        elif operation == '/':
            if operand2 == 0:
                return 'Division by zero'
            else:
                return operand1 / operand2
        else:
            if operation in ('+', '-', '*', '/', '**'):
                return operation
            else:
                return 'Wrong symbol'


count = input('Enter number values: ')

try:
    count = int(count)
except ValueError:
    print('Value must be integers')
else:
    if count == 1:
        operand1 = input('Enter operand1: ')
        print(operand1)
    elif count > 0:
        i = 2

        operand1 = input('Enter operand1: ')
        operation = input('Enter operation: ')
        operand2 = input('Enter operand2: ')

        result = calculate(operand1=operand1,
                           operand2=operand2, operation=operation)

        if isinstance(result, str):
            print(result)
        else:
            while i < count:
                operand1 = result
                operation = input('Enter next operations: ')
                operand2 = input('Enter next operand: ')
                if isinstance(result, str):
                    break
                if operation not in ('+', '-', '*', '/', '**'):
                    break

                result = calculate(operand1=operand1,
                                   operand2=operand2, operation=operation)

                i += 1

            print(result)
    else:
        print('Nothing to calculate')
