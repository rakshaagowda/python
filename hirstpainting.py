#import colorgram
#rgb_colors=[]
#colors=colorgram.extract('image.jpeg',30)
#for color in colors:
 #   r=color.rgb.r
 #   g=color.rgb.g
 #   b=color.rgb.b
 #   new_color=(r,g,b)
 #   rgb_colors.append(new_color)
#
#print(rgb_colors)


import turtle as turtle_module
import random
turtle_module.colormode(255)

tim=turtle_module.Turtle()
#to get rid of the lines
tim.penup()
tim.speed("fastest")
#to remove the turtle symbol
tim.hideturtle()

color_list=[  (231, 222, 91), (119, 175, 204),
 (207, 162, 104), (182, 79, 30), (183, 43, 117), (42, 102, 156), (177, 14, 67), (210, 137, 176), (13, 23, 65),
 (218, 62, 132), (188, 162, 30), (46, 181, 113), (21, 34, 155), (127, 186, 159), (229, 167, 198), (27, 178, 202), (48, 129, 80), (11, 47, 27),
 (52, 22, 12), (146, 216, 196), (134, 216, 228), (232, 221, 8), (74, 11, 31), (161, 24, 13), (221, 80, 49), (111, 94, 202)]


tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100


for dot in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot %10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen=turtle_module.Screen()
screen.exitonclick()
