from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
DENSITY = 35


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def go_up(self):
        new_y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y_cor)

    def reset_pos(self):
        self.setpos(STARTING_POSITION)

    def increase_difficulty(self):
        global DENSITY
        DENSITY = DENSITY * .7

    def report(self):
        return round(DENSITY)
