import random
#import art


logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""


print(logo)


print("Welcome to number guessing game\nI'm thinking of a number between 1 - 100\ntry to guess it ")

level=input("type 'easy' for easy level and 'hard for hard level of the game  ")
if level == "easy":
    attempts=10
else:
    attempts=5


choice=random.randint(1,100)

guess=0
while guess!= choice and attempts>0:

    guess = int(input(f"You have {attempts} guess(es)Make a guess: "))
    attempts=attempts-1
    if guess>choice:
        print("TOO high")
    elif guess<choice:
        print("Too low ")
print(f"it was {choice}. ")
if guess == choice:
    print("YOU WIN")
elif guess != choice:
    print("YOU LOSE")




