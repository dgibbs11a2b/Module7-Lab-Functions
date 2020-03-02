#----------------------------------------
#David Gibbs
#February 28, 2020
#
#This program uses our turtle alex to produce a square of different sizes.
#He will start from one position, create one square and then move further out
#to a different position another square. Each square created will be consecutively
#larger than the previous square. In total, alex will create five squares.
#----------------------------------------

import math
import turtle


wn = turtle.Screen()

alex = turtle.Turtle()
alex.speed(2)
alex.pencolor("blue")
alex.pensize(2)

#This function sets the length of the square and iteration alex will draw
def drawSquare(sz):
    for i in range(4):
        alex.forward(sz)
        alex.left(90)

#defines the main function call
def main():
    sz = 15
    #This sets the length of the initial square that alex will draw
    x = 100
    y = 100
    #This will set alex's x and y coordinates
    
    for i in range(5):
        drawSquare(sz)
        alex.right(90)
        alex.penup()
        alex.forward(10)
        alex.left(90)
        alex.backward(10)
        alex.pendown()
        sz+=20
        #This will set number of squares alex will draw in total and will graudally move to the next
        #starting position until the squares are completed
        wn.exitonclick()
        #This gives the user the ability to exit the screen once the squares have been drawn
main()
#Invokes the main function which will call any other needed functions
