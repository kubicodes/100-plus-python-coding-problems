"""
Category 4 - Conversions

Problem 5: Miles to kilometers
    
The Problem:

Convert miles to kilometers.
"""

"""
Takes in a number as miles.
Converts and returns kilometer value.
"""
def milesToKilometers(miles):
    assert type(miles) != int , "Type in a number!"

    one_mile_to_kilometer = 1.609344
    miles_to_kilometers = miles*one_mile_to_kilometer
    
    return miles_to_kilometers

while True:
    try:
        miles_to_kilometer = float(input("Type in miles. I will convert to Kilometers."))
        break
    except ValueError:
        print("Not a number!")
        continue

kilometers = round(milesToKilometers(miles_to_kilometer), 2)
print("Kilometers:", kilometers)