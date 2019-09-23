def calculator(operand1, operand2, operation):
    if operation == '+':
        print('result =', operand1 + operand2)
    elif operation == '-':
        print('result =', operand1 - operand2)
    elif operation == '*':
        print('result =', operand1 * operand2)
    elif operation == '/':
        if operand2 == 0:
            print('Divided by Zero')
        else:
            print('result =', operand1 / operand2)


print('Eneter operand1: ')
operand1 = float(input())
print('Eneter operation: ')
operation = input()
print('Eneter operand2: ')
operand2 = float(input())


calculator(operand1, operand2, operation)
