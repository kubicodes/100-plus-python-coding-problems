"""
Category 4 - Conversions

Problem 4: Decimal to Binary Recursive
    
The Problem:

Convert a decimal number to binary number using recursion.
"""

"""
Takes in a decimal number as input and converts it to binary number.
Returns the binary number in string format.
"""
def decimalToBinaryRecursive(decimal):
    if decimal == 0:
        return '0'
    elif decimal == 1:
        return '1'
    else:
        return decimalToBinaryRecursive(decimal//2) + str(decimal%2)

try:
    user_decimal_number = int(input("Type in your number wich you want to convert."))
except:
    raise ValueError("Not a number.")

print('Your binary number is: ', decimalToBinaryRecursive(user_decimal_number))