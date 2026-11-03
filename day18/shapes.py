from turtle import Turtle,Screen,colormode
import random
me=Turtle()
no_sides=3
x=colormode(255)
def color_():
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    color=(r,g,b)
    return color

def do(no_sides):
    angle=360/no_sides
    if no_sides<11:
        me.color(color_())
        me.pensize(10)
        for _ in range (no_sides):
            me.forward(100)
            me.left(angle)
        no_sides+=1
        do(no_sides)
do(no_sides)
