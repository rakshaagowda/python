import turtle

#few concepts of object oriented programming like creating object
#concepts of classes are explained


"""constructing object (timmy) 'turtle' is imported and 
from which class 'Turtle' is fetched
timmy=turtle.Turtle()
print(timmy)"""

#or
#attributes
from turtle import Turtle,Screen

timmy =Turtle()
timmy.shape("turtle") #changes shape
timmy.color("coral")#changes color
#to make the turtle move in a triangular shape
for i in range(0,3):
    timmy.forward(100)
    timmy.left(120)#method left has argument angle

my_screen=Screen()
print(my_screen.canvheight)


#methods eg:object.mathod() just likefunction methodalong with object  doessomething
my_screen.exitonclick()
