def validateInputs(first_value,second_value,third_value):
    while (first_value != int) and (second_value != int) and (third_value != int):
        if (first_value != int(first_value)):
            first_value = int(input('Error: Please enter an integer number:'))
        if (second_value != int(second_value)):
            second_value = int(input('Error: Please enter an integer number:'))
        if (third_value != int(third_value)):
            third_value = int(input('Error: Please enter an integer number:'))

def validateOperations(first_operation,second_operation):
    operations_list = ['+','-','*','/']
    while not (first_operation in operations_list) and (second_operation in operations_list):
        if (first_operation not in operations_list):
            first_operation = input('Error: Please enter a valid operation:')
        if (second_operation not in operations_list):
            second_operation = input('Error: Please enter a valid operation:')


first_value = float(input('Enter the first value:'))
first_operation = input('Enther the first operator:')
second_value = float(input('Enter the second value:'))
second_operation = input('Enter the second operator:')
third_value = float(input('Enter the third value:'))

validateInputs(first_value,second_value,third_value)
validateOperations(first_operation,second_operation)

print(f'Enter expression: {first_value} {first_operation} {second_value} {second_operation} {third_value}')
