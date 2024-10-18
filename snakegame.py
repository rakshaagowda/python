from turtle import Turtle,Screen
import time
#setting up snake body
screen =Screen()

screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)
screen.setup(width=600,height=600)
cordinates=[(0,0),(-20,0),(-40,0)]
segments=[]

for position in cordinates:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)
#getting the snake to move
game_is_on=True
while game_is_on:
    screen.update()

    for seg in segments:
        seg.forward(20)
        time.sleep(0.1)
        #range function syntax : range(start=3,stop=0,step=-1)
        for seg_num in range(len(segments)-1,0,-1):
            #made the body follow the head
            new_x=segments[seg_num-1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x,new_y)
        segments[0].forward(20)
    
    
    
    
    
    
    
    
    
    
    
screen.exitonclick()