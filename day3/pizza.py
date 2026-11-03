print("Welcome to the pizza deliveries...!")
size=str(input("what size pizza do you want: S,M or L:"))
pepporoni=input("do you want pepporoni on the pizza Y or N:")
cheese=input("do you want extra cheese on the pizza:")
bill=0
if size== "S" :
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("Wrong Input")
if pepporoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if cheese=="Y":
    bill+=1
print(f"Your Bill is:{bill}")

a=12




    
