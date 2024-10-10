import random
import turtle as t

tim=t.Turtle()
screen=t.Screen()
screen.exitonclick()
tim.shape("turtle")
colours=["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

"""taking turtle to jog (drawing dash line)"""
for _ in range(15):
    tim.color("pink")
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

"""Drawing different shapes"""

def draw_shapes(num_sides):
    angle = (360 / num_sides)

    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_sides in range(3,11):
    tim.color(random.choice(colours))
    draw_shapes(shape_sides)

"""taking turtle for a random walk"""
tim.pensize(10)
direction=[0,90,180,270]
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(direction))