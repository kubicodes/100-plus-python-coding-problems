"""
Category 1 - Easy Ones

2: Math Power

The problem
Take two numbers from the users. Calculate the result of second number power of the first number.
"""

base_number = int(input("Type an integer as the base number."))
power_number = int(input("Type an integer as the power number."))

"""
Takes in two numbers as argument. The first number is the base number and the second number is
the power of the first number. It returns the result of second number power of the first number.
"""

def power_of_two_numbers(base, power):
    return base**power

print(power_of_two_numbers(base_number, power_number))