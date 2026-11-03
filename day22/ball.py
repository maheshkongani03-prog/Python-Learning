from turtle import Turtle 
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()   
        self.new_x=10
        self.new_y=10 
        self.ball_speed=0.1
    def move(self):
        x_cor=self.xcor()+self.new_x
        y_cor=self.ycor()+self.new_y
        self.goto(x_cor,y_cor)
    def bounce_y(self):
        self.new_y=-self.new_y
    def bounce_x(self):
        self.new_x=-self.new_x
        self.ball_speed*=0.9
    def refresh_ball(self):
        self.goto(0,0)
        self.ball_speed=0.1
        self.bounce_x()