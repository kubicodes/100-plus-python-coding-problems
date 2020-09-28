"""
Category 3 - Loop Related

Problem 5: Largest Element of a List

The Problem:

Find the largest element of a list.
"""

"""
Input must be a list of numbers.
Returns the largest value of the list
"""
def largestElement(listOfNumbers):
    assert not type(listOfNumbers) != list, ('You have to give a list as input.')
    
    largest_element = listOfNumbers[0]

    for i in listOfNumbers:
        if i > largest_element:
            largest_element = i
    
    return largest_element


list_of_numbers = [3,5,-2,94,3,7]
print("The largest element is", largestElement(list_of_numbers))