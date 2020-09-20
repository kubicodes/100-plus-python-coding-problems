"""
Category 2 - Number Related

5: Max of two

The Problem:

Find the max number of two numbers.
"""

"""
Takes in two numbers as input and returns the max number.
Returns -1 if inputs are equal
"""
def findMaxOfTwoNumbers(number_1, number_2):
    if number_1 > number_2:
        return number_1
    elif number_2 > number_1:
        return number_2
    else:
        return -1
    
number_1 = int(input("Type in the first number"))
number_2 = int(input("Type in the second numnber"))

max_number = findMaxOfTwoNumbers(number_1, number_2)
print("The max is: " + str(max_number))