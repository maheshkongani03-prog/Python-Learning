import turtle as t
timmy=t.Turtle()
screen=t.Screen()
def forward():
    timmy.forward(100)
def backward():
    timmy.backward(100)
def counter():
    t.mode("standard")
    timmy.forward(100)
    
screen.listen()
screen.onkey(key="a",fun=forward)
screen.onkey(key="b",fun=backward)
screen.onkey(key="c",fun=counter)
screen.exitonclick()