import turtle
import random


screen=turtle.Screen()


screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="which turtle do you think would win the race? enter a colour: ")
colors=["red","orange","yellow","green","blue","purple"]
for turtle_index in range(0,5):
    tim = turtle.Turtle()
    tim.color(colors[turtle_index])
    tim.penup()
    tim.shape("turtle")
    tim.goto(x=-238, y=random.choice(range(-100,200)))


screen.exitonclick()