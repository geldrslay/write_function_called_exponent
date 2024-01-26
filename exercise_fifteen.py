# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

# Defining function
def calculate_exponent (base, exponent):
    if type (exponent) == int and exponent <0:
        print ("Please enter a non-negative exponent")    
    elif exponent == 0:
        return 1
    else:
        return base ** exponent

# Ask user to input base and exponent. 
base = int(input ("Enter base:"))
exponent = int (input ("Enter non-negative exponent:"))

# Display the result 
print (base, "raised to the power of", exponent, "is:",calculate_exponent(base, exponent))

