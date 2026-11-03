print("Welcome to the Treasure Island....!")
direction=input("Where do you want to go Left or Right:")
if direction=="Left":
    motion=input("What do you want to do swim or wait:")   
    if motion=="wait":
        door=input("What door would you choose Red or Blue or Yellow:")
        if door=="Red":
            print("Burned by fire.Game over")
        elif door =="Blue":
            print("Eaten by beasts.Game Over")
        elif door=="Yellow":
            print("You win")
        else :
            print("Game Over")
    else:
        print("you got atacked by angry trout.Game Over")
else:
    print("Fall into a hole. Game Over")
