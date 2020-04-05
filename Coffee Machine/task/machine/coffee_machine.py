# Write your code here
class CoffeeMachine:
    coffee = [
        {"water": 250, "milk": 0, "coffee_beans": 16, "price": 4},  # espresso
        {"water": 350, "milk": 75, "coffee_beans": 20, "price": 7},  # latte
        {"water": 200, "milk": 100, "coffee_beans": 12, "price": 6}  # cappuccino
    ]

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cup = 9
        self.money = 550

    def remaining(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.disposable_cup} of disposable_cups
${self.money} of money""")

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def fill(self):
        print("Write how many ml of water do you want to add:")
        refill = int(input())
        self.water += refill
        print("Write how many ml of milk do you want to add:")
        refill = int(input())
        self.milk += refill
        print("Write how many grams of coffee beans do you wants to add:")
        refill = int(input())
        self.coffee_beans += refill
        print("Write how many disposable cups of coffee do you want to add:")
        refill = int(input())
        self.disposable_cup += refill

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        choice = input()
        if choice != "back":
            choice = int(choice)
            if self.water < self.coffee[choice - 1]["water"]:
                print("Sorry, not enough water!")
            elif self.milk < self.coffee[choice - 1]["milk"]:
                print("Sorry, not enough milk!")
            elif self.coffee_beans < self.coffee[choice - 1]["coffee_beans"]:
                print("Sorry, not enough coffee beans!")
            elif self.disposable_cup < 1:
                print("Sorry, not enough coffee beans!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= self.coffee[choice - 1]["water"]
                self.milk -= self.coffee[choice - 1]["milk"]
                self.coffee_beans -= self.coffee[choice - 1]["coffee_beans"]
                self.disposable_cup -= 1
                self.money += self.coffee[choice - 1]["price"]

    def start(self):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        while action != "exit":
            print()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()

            print()
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()


coffee_machine = CoffeeMachine()
coffee_machine.start()
