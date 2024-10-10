

import random
import turtle as t

tim=t.Turtle()
t.colormode(255)

tim.shape("turtle")


def random_colour():
    r=random.randint(0,255)
    g= random.randint(0, 255)
    b =random.randint(0, 255)
    color =(r,g,b)
    return color

tim.speed("fastest")
def draw_spiral(size_gap):
    for _ in range(int(360/size_gap)):
        tim.circle(100)
        tim.color(random_colour())
        tim.setheading(tim.heading() + size_gap)

draw_spiral(5)

screen=t.Screen()
screen.exitonclick()



