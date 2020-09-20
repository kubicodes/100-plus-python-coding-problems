"""
Category 1 - Easy Ones

5: Temporary Variable

The Problem:

Swap two variables.
To swap two variables: the value of the first variable will become the value of the second variable. 
On the other hand, the value of the second variable will become the value of the first variable.
"""

var_a = 5
var_b = 3


temp = var_a
var_a = var_b
var_b = temp
print("A is swapped to B: " + str(var_a) + " and B is swapped to A: " + str(var_b))
    
