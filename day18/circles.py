import turtle as t

tim=t.Turtle()
tim.speed("fastest")
head=0
for i in range(100):
    tim.circle(80)
    
    tim.setheading(head)
    head+=10




screen=t.Screen()
screen.exitonclick()