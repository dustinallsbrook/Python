from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # Detect collision
    if ball.ycor() > 287 or ball.ycor() < -287:
        ball.bounce_ball_y()

    # Right bounce
    if ball.xcor() > 320 and ball.distance(r_paddle) < 63 and ball.bounce_tracker == 0:
        ball.bounce_ball_x()
        ball.bounce_tracker = 1

    if ball.xcor() < -320 and ball.distance(l_paddle) < 63 and ball.bounce_tracker == 1:
        ball.bounce_ball_x()
        ball.bounce_tracker = 0

    # Detect R paddle missing
    if ball.xcor() > 340:
        ball.ball_reset()
        scoreboard.l_point()
        # ball.speed_up()

    if ball.xcor() < -340:
        ball.ball_reset()
        scoreboard.r_point()
        # ball.speed_up()

    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_on = False
        scoreboard.game_over()

screen.exitonclick()
