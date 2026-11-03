from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class CarManager():
    def __init__(self):
        self.cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE 
        print(f"init {self.car_speed}")
    def create_car(self):
        random_number=random.randint(1,6)
        if random_number==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            car_color=random.choice(COLORS)
            new_car.color(car_color)
            y_cor=random.randint(-250,250)
            new_car.goto(300,y_cor)
            self.cars.append(new_car)   
            
    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
    def speed_up(self):
        self.car_speed+=MOVE_INCREMENT
        print(f"speed in sepped_up is {self.car_speed}") 
        
        


        