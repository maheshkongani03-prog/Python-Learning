import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(fun=player.go_up,key="Up")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for  car in car_manager.cars:
        if abs(player.xcor() - car.xcor()) <= 18 and abs(player.ycor() - car.ycor()) <= 26 :  
            scoreboard.game_Over()     
            game_is_on = False
    
    if player.ycor()>250:
        player.refresh_player()
        car_manager.speed_up()
        player.player_Speed_up()
        scoreboard.update_score()
screen.exitonclick()