from menu_resource import *

water = int(resources["water"])
milk = int(resources["milk"])
coffee = int(resources["coffee"])
score = 0
def report(water, milk, coffee):
    print(water)
    print(milk)
    print(coffee)
    print(f"your profit {score}")

def machine(ask, quarter, dime, nickle, penny):

    total_money = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
    if total_money < MENU[ask]["cost"]:
        return "sorry that's not enough money"
    else:
        global water, milk, coffee, score
        chain = total_money - MENU[ask]["cost"]
        water = water - MENU[ask]["ingredients"]["water"]
        milk = milk - MENU[ask]["ingredients"]["milk"]
        coffee = coffee - MENU[ask]["ingredients"]["coffee"]
        score += MENU[ask]["cost"]

        print("Thank you")
        return f"chain {chain}"


def check_resouce(water, milk, coffee):


    if water < MENU[ask]["ingredients"]["water"]:
        print("there is not enough water")
        return False
    elif milk < MENU[ask]["ingredients"]["milk"]:
        print("there is not enough milk")
        return False
    elif coffee < MENU[ask]["ingredients"]["coffee"]:
        print("there is not enough coffee")
        return False
    else:
        return True


while True:
    ask = input("What would you like?")

    if ask == "report":
        report(water, milk, coffee)
    else:
        print(MENU[ask])
        check = check_resouce(water, milk, coffee)

        if check:
            print("Please insert coin")
            quarter = int(input("how many quarter? "))
            dime = int(input("how many dime? "))
            nickle = int(input("how many nickle? "))
            penny = int(input("how many penny? "))
            print(machine(ask, quarter, dime, nickle, penny))






