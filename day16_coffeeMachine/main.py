from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()
coffee_maker.report()
money_machine.report()
should_continue=True
while should_continue:
    options=menu.get_items()
    choice=input(f"What do you want ({options}):").lower()
    
    if choice =='off':
        should_continue=False
    elif choice=='report':
        report=coffee_maker.report()
        report=money_machine.report()
    else:
        drink=menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink)==True:
            if money_machine.make_payment(drink.cost)==True:
                    coffee_maker.make_coffee(drink)
        


            
