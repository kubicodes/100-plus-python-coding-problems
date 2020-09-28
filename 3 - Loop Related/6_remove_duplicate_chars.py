"""
Category 3 - Loop Related

Problem 6: Remove duplicate chars

The Problem:

For a given string, remove all duplicate characters from that string.
"""

"""
Takes in a string as input.
Returns a new string removed duplicate chars.
"""
def removeDuplicateChar(string):
    assert not type(string) != str, ('You have to give a String as input.')
    
    resultstring = ''
    
    for char in string:
        if char not in resultstring:
            resultstring += char
    
    return resultstring

string = input("Type in a string. I will remove all duplicate characters.")
print('String without duplicates:', removeDuplicateChar(string))
