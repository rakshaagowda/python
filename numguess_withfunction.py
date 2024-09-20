import random
#import art

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""


print(logo)

def difficulty():
    level = input("type 'easy' for easy level and 'hard for hard level of the game  ")
    if level == "easy":
        no_guesses = 10
    else:
        no_guesses = 5

    return no_guesses

def compare(nthguess):
     if nthguess > choice:
         return print("TOO high")

     elif nthguess < choice:
         return print("Too low ")


choice=random.randint(1,100)


def game():
    print("Welcome to number guessing game\nI'm thinking of a number between 1 - 100\ntry to guess it ")

    attempts = difficulty()
    guess = 0
    while guess != choice and attempts > 0:
        guess = int(input(f"You have {attempts} guess(es)Make a guess: "))
        attempts = attempts - 1
        compare(guess)

    print(f"it was {choice}. ")
    if guess == choice:
        print("YOU WIN")
    elif guess != choice:
        print("YOU LOSE")

game()





