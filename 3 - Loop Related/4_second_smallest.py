"""
Category 3 - Loop Related

Problem 5: Second Smallest

The Problem:

For a list, find the second largest number in the list.
"""

"""
Takes in a list of numbers as value.
Returns the second smallest number of the list
"""
def findSecondSmallest(list_of_numbers):
    assert not type(list_of_numbers) != list, ('You have to give a list as input.')
    
    smallest_element = list_of_numbers[0]
    second_smallest_element = list_of_numbers[0]

    for current_number in list_of_numbers:
        if current_number < smallest_element:
            second_smallest_element = smallest_element
            smallest_element = current_number
        elif current_number < second_smallest_element:
            second_smallest_element = current_number
    
    return second_smallest_element

"""
Asks the user to create a list with numbers.
Returns the list
"""
def askUserForListOfNumbers():
    list_of_numbers = []
    try:
        while True:
            len_of_numbers = int(input("How much numbers would you like to enter?"))
            if len_of_numbers <= 0:
                print("You have to type a number that is greater than 0")
                continue
            else:
                break
            
        for i in range(0, len_of_numbers):
            while True:
                try:
                    current_user_input = int(input("Type in the number"))
                    list_of_numbers.append(current_user_input)
                    break
                except ValueError:
                    print("No Valid Value. Try again")
                    continue     
    except Exception:
        print("Something went wrong.")
    
    return list_of_numbers

#--------Main Program---------#

list_of_numbers = askUserForListOfNumbers()
second_largest_element = findSecondSmallest(list_of_numbers)
print("The second smallest element is:", second_largest_element)
        