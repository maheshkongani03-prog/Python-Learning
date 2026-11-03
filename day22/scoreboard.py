from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Left_Score=0
        self.Right_Score=0
        self.calculate_score()
    def calculate_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.Left_Score,align="center",font=("courier",60,"normal"))
        self.goto(100,200)
        self.write(self.Right_Score,align="center",font=("courier",60,"normal"))
    def calculate_left_score(self):
        self.Left_Score+=1
        self.calculate_score()
        
    def calculate_right_score(self):
        self.Right_Score+=1
        self.calculate_score()
        
    