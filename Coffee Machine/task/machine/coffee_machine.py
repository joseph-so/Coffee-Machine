# Write your code here
water = 1200
milk = 540
coffee_beans = 120
disposable_cup = 9
money = 550

print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cup} of disposable_cups
{money} of money""")
print()

coffee = [
    {"water": 250, "milk": 0, "coffee_beans": 16, "price": 4},  # espresso
    {"water": 350, "milk": 75, "coffee_beans": 20, "price": 7},  # latte
    {"water": 200, "milk": 100, "coffee_beans": 12, "price": 6}  # cappuccino
]

print("Write action (buy, fill, take):")
action = input()

if action == "buy":
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    choice = int(input())
    water -= coffee[choice - 1]["water"]
    milk -= coffee[choice - 1]["milk"]
    coffee_beans -= coffee[choice - 1]["coffee_beans"]
    disposable_cup -= 1
    money += coffee[choice - 1]["price"]
elif action == "fill":
    print("Write how many ml of water do you want to add:")
    fill = int(input())
    water += fill
    print("Write how many ml of milk do you want to add:")
    fill = int(input())
    milk += fill
    print("Write how many grams of coffee beans do you wants to add:")
    fill = int(input())
    coffee_beans += fill
    print("Write how many disposable cups of coffee do you want to add:")
    fill = int(input())
    disposable_cup += fill
elif action == "take":
    print(f"I gave you ${money}")
    money = 0

print()
print(f"""The coffee machine has:
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{disposable_cup} of disposable_cups
{money} of money""")
