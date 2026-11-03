from turtle import Turtle,Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.player_speed=MOVE_DISTANCE
    def go_up(self):
        self.forward(self.player_speed)
    def refresh_player(self):
        self.goto(STARTING_POSITION)
    def player_Speed_up(self):
        self.player_speed+=MOVE_DISTANCE

    
    



        

