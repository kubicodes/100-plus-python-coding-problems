"""
Category 1 - Easy Ones

1: User input to Number

The problem
Take two inputs from the user. One will be an integer. 
The other will be a float number. Then multiply them to display the output.
"""

input_integer = int(input("Type in an integer: "))
input_float = float(input("Type a float:"))

"""
Takes in two numbers as argument and returns the multiplied value of this two numbers.
"""
def multiply_two_numbers(number1, number2):
    return number1*number2

print("Multiplied the two inputs: " + str(multiply_two_numbers(input_integer, input_float)))