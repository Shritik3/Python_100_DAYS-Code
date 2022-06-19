from ing import MENU
from ing import resources
from ing import profit
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# user_choice=input('What would you like to have? (espresso,latte,cappuccino):')
# money=0
# def coffee_machine():
#     if user_choice=='report':
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${money}")
#     elif user_choice=='espresso':
#         resources['water']=resources['water']-MENU['espresso']['ingredients']['water']
#         resources['coffee'] = resources['coffee'] - MENU['espresso']['ingredients']['coffee']
#         resources['milk'] = resources['milk'] - MENU['espresso']['ingredients']['milk']
#     elif user_choice=='latte':
#         resources['water'] = resources['water'] - MENU['latte']['ingredients']['water']
#         resources['coffee'] = resources['coffee'] - MENU['latte']['ingredients']['coffee']
#         resources['milk'] = resources['milk'] - MENU['latte']['ingredients']['milk']
#     elif user_choice=='cappuccino':
#         resources['water'] = resources['water'] - MENU['cappuccino']['ingredients']['water']
#         resources['coffee'] = resources['coffee'] - MENU['cappuccino']['ingredients']['coffee']
#         resources['milk'] = resources['milk'] - MENU['cappuccino']['ingredients']['milk']
# print(MENU['espresso']['ingredients']['water'])