#Catching Exceptions
#You can use a try/except block in Python to catch any exceptions that might occur.
#  For example if you imagine there could be a chance of user error.
#  You can prevent it crashing your code by anticipating it.
#  You trap the dangerous code inside a try block and use an except block to catch any potential errors.
#  Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.

#e.g.
#age = int(input("How old are you?"))
#if age > 18:
#    print(f"You can drive at age {age}.")
#produces ValueError which is fixed

try:
    age = int(input("How old are you?"))

except ValueError:
    print("You have entered invalid input try entering number like 15")
    age = int(input("How old are you?"))

if age > 18:
     print(f"You can drive at age {age}.")


