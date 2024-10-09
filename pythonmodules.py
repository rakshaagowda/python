#basic information about importing python module
"""
import modulename
usage:
object=modulename.class_name()
OR
from modulename import class_name
eg: from turtle import Turtle
usage:
object=class_name

to import everything from the module 
from modulename import *
"""

#Aliasing module : naming module
"""
import modulename as m
usage:object=m.class_name() 
eg: import turtle as t
    tim=t.Turtle()
"""
import heroes
print(heroes.gen())