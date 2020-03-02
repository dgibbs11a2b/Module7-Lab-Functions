#----------------------------------------
#David Gibbs
#February 28, 2020
#
#This program uses our turtle alex to produce a 6 sided polygon
#flower on the screen, cmpared to our assignment.
#It will repeat the sequence 12 times.
#----------------------------------------


import turtle                                                        

wn = turtle.Screen()
#creates a canvas for alex to draw                                                    
                                                       

def flowerPolygon(alex):
    for i in range(12):     
#This function draws a flower by repeating a 6 sided polygons
#in sequence twelve times
        alex.forward(50)
        alex.left(50)
        alex.forward(50)
        alex.left(50)
        alex.forward(50)
        alex.left(50)
        alex.forward(50)
        alex.left(50)
        alex.forward(50)
        alex.left(50)
        alex.forward(50)
        alex.left(50)
        # This moves alex to the left 30 degrees before the sequence starts again 
        alex.left(30)
 
def main():       
#defines the main function call
    alex = turtle.Turtle()    
    alex.speed(5)
    alex.pencolor("hot pink")
    alex.pensize(2)
    flowerPolygon(alex)

    wn.exitonclick()
    # create a turtle named alex, sets the pen size, pen color
    #and then intiates flowerPolygon. Provides click on exit.
main()
#invokes main
