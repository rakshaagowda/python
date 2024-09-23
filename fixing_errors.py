#Catching Exceptions
"""You can use a try/except block in Python to catch any exceptions that might occur.
For example if you imagine there could be a chance of user error.
You can prevent it crashing your code by anticipating it.
You trap the dangerous code inside a try block and use an except block to catch any potential errors.
Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.

#e.g.
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")
produces ValueError which is fixed"""

try:
    age = int(input("How old are you?"))

except ValueError:
    print("You have entered invalid input try entering number like 15")
    age = int(input("How old are you?"))

if age > 18:
     print(f"You can drive at age {age}.")

#USE PRINT
"""print() is your friend. It can help expose hidden values while your code is running.
 In a for loop, the loop will follow some rules to perform a repeated block of code.
   But during the loop it's difficult to see the intermediate values,
that's a perfect example of how you can use print to expose those intermediate values and help you debug your code."""

"""The code is supposed to calculate the total number of words given the number pages and the word per page.
 But it's not currently giving any output. 
 Diagnose the problem using print() statements"""

#eg
"""word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))

total_words = pages * word_per_page
print(total_words)"""

#prints zero 

word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

#when word_per_page is printed it is noted that there was issue with assignment operator

#USING DEBUGGER

"""Most IDEs (Intelligent Development Environments) such as PyCharm will have built-in tools for debugging.
This is normally known as the debugger. In many ways, they are like print statements on steroids.

Debuggers allows us to peek into our code during execution and pause on chosen lines
 to figure out what is the inner mechanism and where it's going wrong.

There are a couple of things that are the same in most IDEs which you should be familiar with:

Breakpoint - You can set a breakpoint by clicking on a line in the gutter of the code (where the line numbers are).
 This line will be where the program pauses during debug run.

Step Over - This button will go through the execution of your code line by 
 and allow you to view the intermediate values of your variables.

Step Into - This will enter into any other modules that your code references. 
e.g. If you use a function from the random module it will show you the original code for that function 
so you can better understand its functionality and how it relates to your problems.

Step Into My Code - This does the same thing as Step Into, 
but it limits the scope to your own project code and ignores library code such as random.

Use the PyCharm debugger to figure out what is the issue in the starting code and fix it."""