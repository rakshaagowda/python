#turtle race using higher order functions 
import turtle

tim=turtle.Turtle()

screen=turtle.Screen()


def move_forward():
    tim.forward(10)
screen.listen()
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()