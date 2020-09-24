"""
Category 2 - Number Related

3: Average of numbers

The Problem:

Take numbers from a user and show the average of the numbers the user entered.
"""


len_of_numbers = int(input("How many numbers do you want to enter?"))

numbers = []

for i in range(len_of_numbers):
    current_user_input = int(input("Type in the number: "))
    numbers.append(current_user_input)

sum_of_numbers = sum(numbers)
average = sum_of_numbers/len_of_numbers

print("The average is: " + str(average))