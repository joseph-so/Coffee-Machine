# Write your code here
required_water = 200
required_milk = 50
required_coffee_beans = 15

print("Write how many ml of water the coffee machine has:")
water = int(input())

print("Write how many ml of milk the coffee machine has:")
milk = int(input())

print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())

print("Write how many cups of coffee will you need:")
cup = int(input())

no_of_cup = min(water // required_water, milk // required_milk, coffee_beans // required_coffee_beans)

if no_of_cup < cup:
    print(f"No, I can make only {no_of_cup} cups of coffee")
else:
    print("Yes, I can make that amount of coffee", end='')
    print(f" (and even {no_of_cup - cup} more than that)" if no_of_cup > cup else "")
