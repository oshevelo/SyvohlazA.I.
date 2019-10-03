from simpleeval import simple_eval

def calculate(s):
    try:
        s = simple_eval(s)
    except Exception as e:
        return e
    else:
        return s

count = input('Enter number values: ')

calculate_expression = ''

try:
    count = int(count)
except ValueError:
    print("Values must be integer")
else:
    if count == 1:
        operand1 = input('Enter the operand1: ')
        print(operand1)
    elif count > 0:
        calculate_expression+=(input('Enter the operand2: '))

        for i in range(1, count):
            calculate_expression+=(input('Enter the next_operation: '))
            calculate_expression+=(input('Enter the next_operand: '))

        print('result =', calculate(calculate_expression))

    else:
        print('Nothing to calculate!')
