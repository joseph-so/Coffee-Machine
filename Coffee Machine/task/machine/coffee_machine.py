# Write your code here
water = 400
milk = 540
coffee_beans = 120
disposable_cup = 9
money = 550

coffee = [
    {"water": 250, "milk": 0, "coffee_beans": 16, "price": 4},  # espresso
    {"water": 350, "milk": 75, "coffee_beans": 20, "price": 7},  # latte
    {"water": 200, "milk": 100, "coffee_beans": 12, "price": 6}  # cappuccino
]


def remaining():
    print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cup} of disposable_cups
${money} of money""")


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


def fill():
    global water, milk, coffee_beans, disposable_cup
    print("Write how many ml of water do you want to add:")
    refill = int(input())
    water += refill
    print("Write how many ml of milk do you want to add:")
    refill = int(input())
    milk += refill
    print("Write how many grams of coffee beans do you wants to add:")
    refill = int(input())
    coffee_beans += refill
    print("Write how many disposable cups of coffee do you want to add:")
    refill = int(input())
    disposable_cup += refill


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = input()
    if choice != "back":
        choice = int(choice)
        global water, milk, coffee_beans, disposable_cup, money
        if water < coffee[choice - 1]["water"]:
            print("Sorry, not enough water!")
        elif milk < coffee[choice - 1]["milk"]:
            print("Sorry, not enough milk!")
        elif coffee_beans < coffee[choice - 1]["coffee_beans"]:
            print("Sorry, not enough coffee beans!")
        elif disposable_cup < 1:
            print("Sorry, not enough coffee beans!")
        else:
            print("I have enough resources, making you a coffee!")
            water -= coffee[choice - 1]["water"]
            milk -= coffee[choice - 1]["milk"]
            coffee_beans -= coffee[choice - 1]["coffee_beans"]
            disposable_cup -= 1
            money += coffee[choice - 1]["price"]


print("Write action (buy, fill, take, remaining, exit):")
action = input()
while action != "exit":
    print()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "remaining":
        remaining()

    print()
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()



