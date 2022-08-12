from turtle import Turtle
from random import *
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(choice(COLORS))
        self.goto(280, randint(-250, 250))
        self.seth(180)


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_dist = STARTING_MOVE_DISTANCE
        self.cars_ready()

    def add_car(self):
        if randint(0, 100) % 5 == 0:
            new_car = Car()
            self.cars.append(new_car)

    def move_cars(self):
        # move every car
        for car in self.cars:
            car.forward(self.move_dist)  # x is decreased

    def cars_ready(self):
        ready = False
        self.cars.append(Car())
        while not ready:
            if self.cars[0].xcor() < -140:
                ready = True
            else:
                self.move_cars()
                self.add_car()
