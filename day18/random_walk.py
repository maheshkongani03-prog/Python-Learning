import turtle as t
import random 
me=t.Turtle()

t.colormode(255)
me.pensize(15)
directions=[0,90,180,270]
me.speed("fast")
def color_mode():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    colour=(r,g,b)
    return colour
for _ in range(100):
    me.color(color_mode())
    me.forward(30)
    me.setheading(random.choice(directions))

screen=t.Screen()
screen.exitonclick()