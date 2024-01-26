# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# Defining function
def exponent (base, exponent):
    if exponent == 0:
        return 1
    else:
        result = base ** exponent

