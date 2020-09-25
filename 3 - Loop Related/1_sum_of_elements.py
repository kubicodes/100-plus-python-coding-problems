"""
Category 3 - Number Related

Problem 5: Sum of Digits
    
The Problem:

For a given list, get the sum of each number in the list
"""

"""
takes in a list of digits as parameter
returns a number with sum of all elements from the input.

Notice: this should be easily solved by the sum() built-in function. 
But in this solution, I will implement my own function.
This is the extended version of exercise 5 in section 2 with more defensive programming.
"""

"""
Asks the user for integer input always.
Returns a list of all numbers the user typed in.
"""
def getNumbersFromUser():
    while True:
        try:
            len_of_numbers = int(input("Please type in how much numbers you want to sum."))
            break
        except ValueError:
            print("You didn´t type in an integer value. Please try again.")
    
    numbers = []
    
    for i in range(0, (len_of_numbers)):
        while True:
            try:
                current_number = int(input("Type in the number you want to add."))
                break
            except ValueError:
                print("You didn´t type in an integer value. Please try again.")
            
        numbers.append(current_number)
    return numbers

"""
Takes in a list of integers.
Returns the sum of each element in the list.
"""
def sumOfDigits(numbers):
    assert not type(numbers) == list, 'You have to give a list of numbers.'
    sum_of_numbers = 0
    
    for number in numbers:
        sum_of_numbers += number
    
    return sum_of_numbers

numbers_from_user = getNumbersFromUser()
sum_of_user_numbers = sumOfDigits(numbers_from_user)

print("The sum of your numbers is:", sum_of_user_numbers)