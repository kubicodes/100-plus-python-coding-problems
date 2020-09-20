"""
Category 1 - Easy Ones

3: Floor Division

The problem
Find the floor division of two numbers.
"""

number_1 = int(input("Type in the first number."))
number_2 = int(input("Type in the second number."))


"""
Takes in two integers as argument and returns the floor division of this two numbers.
"""
def floor_division(number_1, number_2):
    return number_1//number_2

print(floor_division(number_1, number_2))