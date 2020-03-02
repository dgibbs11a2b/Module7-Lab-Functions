#----------------------------------------
#David Gibbs
#February 27, 2020
#
#This program contains a function to check whether a number is in a given range.
#It uses range(1,10). It will then print a message on the screen
#whether the number is in or is not in the range.
#----------------------------------------

def test_range(n):
    if n in range(1,10):
#sets definition name, parameter, and function for range 1 through 10
        return(" %d is in the range"%int(n)) #used as a placeholder for a numeric value
    else :
        return("The number is outside the given range.")
#returns this string if the number is outside of the range
n = int(input("Enter a number: "))
print(test_range(n))
#tests the input value against the range
