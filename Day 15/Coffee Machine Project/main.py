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

profit = 0

def are_resources_sufficient(coffee):
    for ingredient in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True

def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return total

def is_transaction_successful(coffee, money):
    global profit
    cost = MENU[coffee]["cost"]
    if money < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        profit += cost
        if money > cost:
            change = round((money - cost), 2)
            print(f"Here is ${change} in change.")
        return True


def coffee_machine():
    print("Welcome to the coffee machine!")
    working = True

    while working:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            print("Goodbye!")
            working = False
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            if are_resources_sufficient(choice):
                total = process_coins()
                if is_transaction_successful(choice, total):
                    for ingredient in MENU[choice]["ingredients"]:
                        resources[ingredient] -= MENU[choice]["ingredients"][ingredient]
                    print(f"Here is your {choice} ☕️. Enjoy!")

coffee_machine()