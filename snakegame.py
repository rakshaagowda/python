from turtle import Turtle,Screen
#setting up snake body
screen =Screen()

screen.bgcolor("black")
screen.setup(width=600,height=600)
cordinates=[(0,0),(-20,0),(-40,0)]

for position in cordinates:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    
    
    
    
    
    
    
    
    
    
    
    
screen.exitonclick()