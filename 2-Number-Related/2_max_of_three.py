"""
Category 3 - Number Related

5: Max of three

The Problem:

Find the max number of three numbers.
"""

"""
Takes in three numbers as input and returns the max number.
Returns -1 if inputs are equal
"""

def findMaxOfThreeNumbers(number_1, number_2, number_3):
    if number_1 > number_2 and number_1 > number_3:
        return number_1
    elif number_2 > number_1 and number_2 > number_3:
        return number_2
    elif number_3 > number_1 and number_3 > number_2:
        return number_3
    else:
        return -1

number_1 = int(input("Type in the first number"))
number_2 = int(input("Type in the second number"))
number_3 = int(input("Type in the third number"))

max_number = findMaxOfThreeNumbers(number_1, number_2, number_3)

print("The max number is :" + str(max_number))