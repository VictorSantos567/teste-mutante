# Calculadora

def calculator_option(operation, number_1,number_2):
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        return (number_1 + number_2)
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        return (number_1 - number_2)
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        return (number_1 * number_2)
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        return (number_1 / number_2)
    else:
        return ('You have not typed a valid operator')

# if __name__ == '__main__':
#     operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')
#     number_1 = int(input('Enter your first number> '))
#     number_2 = int(input('Enter your second number> '))

#     result = calculator_option(operation,number_1,number_2)
#     print(result)
