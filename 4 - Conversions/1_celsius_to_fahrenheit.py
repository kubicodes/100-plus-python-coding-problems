"""
Category 4 - Conversions

Problem 5: Celsius to Fahrenheit
    
The Problem:

Take the temperature in degrees Celsius and convert it to Fahrenheit.
"""

"""
Takes in a number as temperature in celsius.
Converts and returns fahrenheit value.
"""
def celsiusToFahrenheit(temperature_in_celsius):
    assert type(temperature_in_celsius) != int , "Type in a number!"
    fahrenheit = ((temperature_in_celsius*9) / 5) + 32
    
    return fahrenheit

while True:
    try:
        temperature_in_celsius = float(input("Type in celsius. I will convert to Fahrenheit."))
        break
    except ValueError:
        print("Not a number!")
        continue

temperature_in_fahrenheit = celsiusToFahrenheit(temperature_in_celsius)
print("In Fahrenheit:", temperature_in_fahrenheit)