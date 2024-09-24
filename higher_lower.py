#The goal is to build a game that asks the user to guess who has more followers on Instagram
import random
#import art
#import game_data

logo='''
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  '''


vs='''
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

'''


def format_account(account):
    account_name=account["name"]
    account_desr=account["description"]
    account_country=account["country"]
    return f"{account_name} ,{account_desr} from {account_country}"

def check_followers(a_followers_count,b_followers_count):
    if a_followers_count>b_followers_count:
        return 'a'
    else:
        return 'b'


print(logo)
score=0
should_continue=True
account_b=random.choice(data)

while should_continue:
    account_a=account_b
    account_b=random.choice(data)
    if account_a == account_b:
        account_b=random.choice(data)

    print(f"COMPARE A {format_account(account_a)}")
    print(vs)
    print(f"B {format_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    print("\n" * 20)
    print(logo)

    a_followers=account_a["follower_count"]
    b_followers=account_b["follower_count"]

    is_correct=check_followers(a_followers,b_followers)
    if is_correct == guess:
        score+=1
        print(f"You were right your score is {score}")

    else:
        print(f"you were wrong your score is {score}")
        should_continue =False




