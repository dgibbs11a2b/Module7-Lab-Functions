#----------------------------------------
#David Gibbs
#February 26, 2020
#
#This program contains a function which prompts you for input of radius (r),
#and then it will print the area of a circle to the screen 
#----------------------------------------

import math
#imports the math module
def areaOfCircle(r):
   return math.pi * r**2
#sets the function definition areaOfCircle, and the parameter (r) and returns
#pi * radius to the second power

r = float(input("Please input the radius of your circle: "))
print(areaOfCircle(r))

#defines (r) and takes user input, multiplies it by pi and displays it
#on the screen 
