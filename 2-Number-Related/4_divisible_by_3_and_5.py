"""
Category 2 - Number Related

Problem 4: Divisible by 3 and 5

The Problem:

For a given number, find all the numbers smaller than the number. 
Numbers should be divisible by 3 and also by 5.
"""

def divisibleBy3And5(num):
    smaller_nums_div_3_and_5 = []
    
    #base case
    if num in range(0,3):
        print("Your number is too small so it can´t be divided by 3 and 5. ")
        
    for i in range(3, num):
        if i%3 == 0 and i%5 == 0:
            smaller_nums_div_3_and_5.append(i)
    
    return smaller_nums_div_3_and_5

num = int(input("Type in your number: "))

divisible_by_3_and_5 = divisibleBy3And5(num)
print("All smaller numbers of your number wich are divisible by 3 and also by 5", divisibleBy3And5(num))