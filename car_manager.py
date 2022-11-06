from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_increment = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_car = random.randint(1, 6)
        if random_car == 1:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.move_increment)

    def increase_speed(self):
        self.move_increment += MOVE_INCREMENT
