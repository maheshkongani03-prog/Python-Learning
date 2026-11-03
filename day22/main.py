from turtle import Turtle,Screen 
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(False)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball =Ball()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

is_game_on=True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #collisions with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #collisions with paddle
    if ball.xcor()>320 and ball.distance(r_paddle)<50 or ball.xcor()<-320 and ball.distance(l_paddle)<50:
        print("hit paddle")
        ball.bounce_x()
        
    #if right paddle misses ball will go to left side 
    if ball.xcor()>380 :
        ball.refresh_ball()
        scoreboard.calculate_left_score()
    
    #if left paddle misses ball will go to right side 
    if ball.xcor()<-380:
        ball.refresh_ball()
        scoreboard.calculate_right_score()

screen.exitonclick()
