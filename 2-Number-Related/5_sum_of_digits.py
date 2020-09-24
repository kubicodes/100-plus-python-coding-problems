"""
Category 2 - Number Related

Problem 5: Sum of Digits
    
The Problem:

For a given list, get the sum of each number in the list
"""

"""
takes in a list of digits as parameter
returns an integer with sum of all elements from the input.

Notice: this should be easily solved by the sum() built-in function. 
But in this solution, I will implement my own function.
"""
def sum_of_digits(numbers):
    sum_of_all_elements = 0
    
    for number in numbers:
        sum_of_all_elements += number
        
    return sum_of_all_elements

numbers_len = int(input("How much numbers would you like to enter?"))

numbers = []
for i in range(numbers_len):
    current_number = int(input("Type in your number: "))
    numbers.append(current_number)

sum_of_numbers = sum_of_digits(numbers)

print("The sum of your digitis is:", sum_of_numbers)