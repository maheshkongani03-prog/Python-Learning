from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"score:{self.score}",align="center",font=("Arial,24,normal"))
        #self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial,24,normal"))
        
    def calculate_score(self):
        self.score+=1
        self.clear()
        self.write(f"score:{self.score}",align="center",font=("Arial,24,normal"))
        
        
       
        
        


   