#The goal is to build a calculator program.



def add(n1, n2):
    return n1 + n2


def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2


def divide (n1,n2):
    if n2 == 0:
        print("divide by zero error")
        return

    else:
        return n1/n2
def calculator():
    from art import logo
    print(logo)
    should_continue = True
    num1 = float(input("Enter the first number: "))
    while should_continue:


        num2 = float(input("Enter second number: "))

        calculation = {
            "+": add(num1, num2),
            "-": subtract(num1, num2),
            "*": multiply(num1, num2),
            "/": divide(num1, num2)

        }
        for choice in calculation:
            print(choice)

        choice = input("Enter your choice: ")
        answer=calculation[choice]

        print(f"{num1} {choice} {num2} ={calculation[choice]}")
        continue_with_answer = input("type'y' to continue with answer or 'n' ")
        if continue_with_answer == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()
