from Lesson import homework

operand1 = input('Enter operand1: ')
operation = input('Enter operation: ')
operand2 = input('Enter operand2: ')

result = homework.calculator(operand1=operand1, operand2=operand2, operation=operation)

if isinstance(result, str):
    print(result)
