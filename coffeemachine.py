MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True



def process_coins():
    total=int(input("Enter how many quarter: "))*.25
    total += int(input("Enter how many nickel: ")) * .1
    total += int(input("Enter how many dime: ")) * .05
    total += int(input("Enter how many penniesr: ")) * .01


    return total


def is_transaction_successful(money_recieved,drink_cost):
    if money_recieved<drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change=round(money_recieved-drink_cost,2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True

def make_coffee(drink_name,drink_ingredients):
    for item in drink_ingredients:
        resources[item]-=drink_ingredients[item]
    print(f"“Here is your latte. Enjoy!")
profit=0
is_on= True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice =="off":
        is_on=False
    elif choice=="report":
       print(f" Water:{resources['water']}  ")
       print(f" Milk: {resources['milk']}ml")
       print(f" Coffee:{resources['coffee']} ")
       print(f" Money: ${profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])






