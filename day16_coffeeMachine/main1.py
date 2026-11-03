from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()
should_continue=True
while should_continue:
    choice=input(f"what do you want {menu.get_items()}:").lower()
    if choice=="off":
        print("Turning off the Coffee Machine")
        should_continue=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if drink:
            if coffee_maker.is_resource_sufficient(drink)==True:
                if money_machine.make_payment(drink.cost)==True:
                    coffee_maker.make_coffee(drink)
        
