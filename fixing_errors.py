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