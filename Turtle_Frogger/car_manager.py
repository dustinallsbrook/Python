from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = .8
MOVE_INCREMENT = .5


class CarManager:

    def __init__(self):
        self.new_cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1, 2)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        # new_car.setpos(250, -240)
        new_car.setpos(300, random.randint(-250, 250))
        self.new_cars.append(new_car)

    def car_sweep(self):
        for car in self.new_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def car_speed_up(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
