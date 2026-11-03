from turtle import Turtle 
t=Turtle()

def dothis():
    i=1
    while i<5:
        t.color("red")
        t.forward(10)
        t.penup()
        # t.forward(10)
        # t.pendown()
        i+=1
        
for _ in range(4):
    dothis()
    t.left(90)
    


"""
x=Screen()
x.exitonclick()

"""