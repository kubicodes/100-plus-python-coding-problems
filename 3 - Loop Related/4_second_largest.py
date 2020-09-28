"""
Category 3 - Loop Related

Problem 4: Second Largest

The Problem:

For a list, find the second largest number in the list.
"""

"""
Takes in a list of numbers as value.
Returns the second largest number of the list
"""
def findSecondLargest(list_of_numbers):
    assert not type(list_of_numbers) != list, ('You have to give a list as input.')
    
    largest_element = list_of_numbers[0]
    second_largest_element = list_of_numbers[0]

    for current_number in list_of_numbers:
        if current_number >largest_element:
            second_largest_element = largest_element
            largest_element = current_number
        elif current_number > second_largest_element:
            second_largest_element = current_number
    
    return second_largest_element



#--------Main Program---------#
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

second_largest_element = findSecondLargest(list_of_numbers)
print("The second largest element is:", second_largest_element)
        