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
def water_needed(MENU,drink):
    water_amount=MENU[drink]['ingredients']['water']
    return water_amount
def milk_needed(MENU,drink):
    milk_amount=0
    if drink!='espresso':
        milk_amount=MENU[drink]['ingredients']['milk']
        return milk_amount
    else:
     return milk_amount
def coffee_needed(MENU,drink):
    water_amount=MENU[drink]['ingredients']['coffee']
    return water_amount
def cost(MENU,drink):
    to_pay=MENU[drink]['cost']
    return to_pay
def total_given(quarter,dimes,nickel,pennies):
    cost=(quarter*0.25)+(dimes*0.1)+(nickel*0.05)+(pennies*0.01)
    return cost
def change(to_pay,final):
    final_change=final-to_pay
    return final_change
water=resources['water']
milk=resources['milk']
coffee=resources['coffee']
money=0
should_continue=True
while should_continue:
    drink=input("What do You want 'espresso'or 'latte' or 'cappuccino':").lower()
    if drink=="report":
        print(f" water:{water}:\n milk:{milk}\n coffee:{coffee}\n money:{money}")
    elif drink=='off':
        print("the machine is off")
        should_continue=False
        
    elif drink not in MENU:
        print("Invalid Selection. Please choose espresso, latte, or cappuccino.")
        
    elif water<water_needed(MENU,drink):
        print("sorry water is less")
        should_continue=False
        
    elif milk<milk_needed(MENU,drink):
        print("sorry milk is low")
        should_continue=False
     
    elif coffee<coffee_needed(MENU,drink):
        print("sorry coffee is less")
        should_continue=False
        
    else:
        to_pay=cost(MENU,drink)
        print(f"you have to pay:{to_pay}")
        print("Please Insert Coins:")
        quarter=int(input("How many quarters:"))
        dimes=int(input("How many dimes:"))
        nickel=int(input("How many nickels:"))
        pennies=int(input("How many pennies:"))
        money_inserted=total_given(quarter,dimes,nickel,pennies)
        if money_inserted>to_pay:
            change1=change(to_pay,money_inserted)
            water-=water_needed(MENU,drink)
            milk-=milk_needed(MENU,drink)
            coffee-=coffee_needed(MENU,drink)
            print(f"amount inserted:{money_inserted} ")
            print(f"Here's your {drink}")
            print(f"Here's your {change1}")
            money+=to_pay
        elif money_inserted<to_pay:

            print(f"amount inserted:{money_inserted} ")
            print("Sorry That's not enough money.money refunded.please Try again")

        else:
            water-=water_needed(MENU,drink)
            milk-=milk_needed(MENU,drink)
            coffee-=coffee_needed(MENU,drink)
            print(f"amount inserted:{money_inserted} ")
            print("Exact amount received. No change.")
            print(f"Here's your {drink}")
            money+=money_inserted

            







