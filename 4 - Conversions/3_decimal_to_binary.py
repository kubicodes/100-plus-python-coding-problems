"""
Category 4 - Conversions

Problem 3: Decimal to Binary
    
The Problem:

Convert a decimal number to binary number.
"""

"""
Takes in a decimal number as input and converts it to binary number.
Returns the binary number.
"""
def decimalToBinary(decimal):
    binary_list = []
    current_result = decimal

    if decimal == 0:
        binary_list.append(0)
    elif decimal == 1:
        binary_list.append(1)
    else:
        while current_result >= 1:  
            binary_list.append(current_result % 2)
            current_result = current_result // 2
    reversed_list = binary_list[::-1]
    
    str_decimal = ''
    for char in reversed_list:
        str_decimal += str(char)
    
    return int(str_decimal)


try:
    user_decimal_number = int(input("Type in your number wich you want to convert."))
except:
    raise ValueError("Not a number.")

print('Your binary number is: ', decimalToBinary(user_decimal_number))