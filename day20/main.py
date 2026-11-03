from turtle import Screen
from scoreboard import ScoreBoard
import time
from snake import Snake
from food import Food

screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
snake=Snake()
scoreboard=ScoreBoard()
food=Food()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food)<15:
        snake.extend_snake()
        food.refresh()
        scoreboard.calculate_score()
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or  snake.head.ycor()<-280:
        is_game_on=False
        scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            print("collided")
            is_game_on=False
            scoreboard.game_over()

screen.exitonclick()