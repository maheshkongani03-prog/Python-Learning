from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-220,240)
        self.score=0
        self.write(f"Score={self.score}",align="Left",font=(FONT))
    def update_score(self):
        self.clear()
        self.score+=1
        self.write(f"Score={self.score}",align="Left",font=(FONT))
    def game_Over(self):
        self.goto(0,0)
        self.write("Game Over",align="center",font=(FONT))
       