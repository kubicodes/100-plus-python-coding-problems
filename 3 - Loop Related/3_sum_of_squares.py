"""
Category 3 - Loop Related

Problem 3: Sum of Squares

The Problem:

Take a number as input. Then get the sum of the numbers. If the number is n. Then get
"""

"""
Input must be a number.
Returns the sum of the numbers. If the number is n. Then get
0^2+1^2+2^2+3^2+4^2+.............+n^2
"""

def sumOfSquares(number):
    assert not type(number) != int, 'You must type in a number'
    
    sum_of_numbers = 0
    
    for i in range(0,number+1):
        sum_of_numbers += i**2
    
    return sum_of_numbers

while True:
    try:
        user_number = int(input("Type in a number n wich you want to get sum from 0 to n."))
        break
    except ValueError:
        print("Could not convert to a number.")
        continue
        
sum_of_squares = sumOfSquares(user_number)
print(sum_of_squares)    
