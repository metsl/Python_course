from recepies import resources, MENU
from art import logo

income = 0.0

def init():
    '''Initialize the resources and income'''
    global income
    income = 0.0
    resources["water"]= 300
    resources["milk"]= 200
    resources["coffee"]= 100

def check_resources(order):
    '''Check if the resources are sufficient'''
    if resources['water'] < MENU[order]['ingredients']['water']:
        return '  Not enough Water'
    elif resources['milk'] < MENU[order]['ingredients']['milk']:
        return '  Not enough Milk'
    elif resources['coffee'] < MENU[order]['ingredients']['coffee']:
        return '  Not enough Coffee'
    else:
        return 'available'

def check_order(order):
    """Check what user input is given"""
    if order == 'off':
        return False
    elif order == 'report':
        water = resources.get("water")
        milk = resources.get("milk")
        coffee = resources.get("coffee")
        print(f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}\nProfit: {income}")
        return True
    elif order == 'restock':
        resources["water"]= 300
        resources["milk"]= 200
        resources["coffee"]= 100
        print("  All resources are restocked!")
        return True
    elif order == 'espresso' or order == 'latte' or order == 'cappuccino':
        enough_resources = check_resources(order)
        if enough_resources=='available':
            return "get Price"
        else:
            print(f" {enough_resources}")
            return True
    else:
        print("  Invalid Order")
        return True
    
def calc_stock(order):
    '''Recalculate stock'''
    resources["water"] -= MENU[order]['ingredients']['water']
    resources["milk"] -= MENU[order]['ingredients']['milk']
    resources["coffee"] -= MENU[order]['ingredients']['coffee']
    
def transaction(order):
    '''Ask to insert coins, calculate the transaction and give change if needed'''
    print("  Please insert coins!")
    price = MENU[order]['cost']
    print(f"the price of {order} is {price}$ ")
    quarters = int(input("  How many quarters? "))*0.25
    dimes = int(input("  How many dimes? "))*0.1
    nickels = int(input("  How many nickels? "))*0.05
    pennies = int(input("  How many pennies? "))*0.01
    if price> quarters+dimes+nickels+pennies:
        print("  Not enough money!")
    else:
        global income
        income += price
        print(f"  Here is ${round(quarters+dimes+nickels+pennies-price,2)} in change.")
        print(f"  Here is your {order} ☕️ Enjoy!")
        calc_stock(order)

def coffee_machine():
    '''Coffee Machine'''
    print(logo)
    order = input(" What do would you like? (espresso/latte/cappuccino).\nFOR MAINTENANCE ONLY!!! type 'report' to see resources left and type 'off' to restart the machine)): ").lower()
    todo = check_order(order)
    if not todo:
        return
    elif todo == 'get Price':
        transaction(order)
    coffee_machine()

def start_machine():
    '''Driver Program'''
    init()
    coffee_machine()
    if input(" Type 'y' to restart machine, 'n' to exit: ").lower() == 'y':
        print(" " *20)
        start_machine()

start_machine()


