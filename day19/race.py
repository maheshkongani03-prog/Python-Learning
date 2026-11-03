import turtle as t
import random
screen=t.Screen()
user_choice=screen.textinput(title="Make your bet",prompt="What colour do you choose?").lower()
colors=["red","yellow","green","blue","purple","violet"]
screen.setup(500,400)
y=-150
turtles=[]
is_race_on=False
j=0
for i in colors:
    timmy=t.Turtle("turtle")
    timmy.color(colors[j])
    j+=1
    timmy.penup()
    timmy.setposition(-230,y)
    y+=30
    turtles.append(timmy)
if user_choice:
    is_race_on=True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor()>230:
            winning_turtle_color=turtle.pencolor()
            is_race_on=False
            if winning_turtle_color==user_choice:
                print(f"your choice of {user_choice} Turtle Lost the Race! ") 
                print(f"The Winner is {winning_turtle_color} Turtle")
            else:
                print(f"your choice of {user_choice} Turtle Lost the Race! ")
                print(f"The Winner is {winning_turtle_color} Turtle")
        distance=random.randint(0,10)
        turtle.forward(distance)
screen.exitonclick()

