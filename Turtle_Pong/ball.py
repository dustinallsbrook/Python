from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_speed = .005
        self.x_move = 1.5
        self.y_move = 1.5
        self.bounce_tracker = 0

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def bounce_ball_y(self):
        self.y_move *= -1

    def bounce_ball_x(self):
        self.x_move *= -1

    def ball_reset(self):
        self.goto(0, 0)
        self.bounce_ball_x()
        # self.y_move *= -1

    # def speed_up(self):
    #

        # if self.x_move > 0:
        #     self.x_move += .2
        # else:
        #     self.x_move -= .2
        #
        # if self.y_move > 0:
        #     self.y_move += .2
        # else:
        #     self.y_move -= .2


