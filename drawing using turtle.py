#------Drawing using turtle
import turtle
def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #Create the turtle brad - Draws a Square
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    for i in range(1,37):#36 times 360/10 form brad.right(10)
        draw_square(brad)
        brad.right(10)
        
    #Create the turtle Angie - Draws a Circle
    
    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    
    
    
    window.exitonclick()

draw_art()

#turtle documentation link------https://docs.python.org/2/library/turtle.html#
