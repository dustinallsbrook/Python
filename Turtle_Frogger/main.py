import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player1.go_up, key="Up")
# screen.onkey(fun=print(round(player1.report())), key="Left")
n = 0

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()

    if n == player1.report():
        cars.create_car()
        n = 0
    else:
        n += 1

    cars.car_sweep()

    if player1.ycor() == 280:
        scoreboard.player_point()
        player1.reset_pos()
        player1.increase_difficulty()
        cars.car_speed_up()
        n = 0

    for car in cars.new_cars:
        if (car.xcor() - 30 < player1.xcor() < car.xcor() + 30
                and car.ycor() - 15 < player1.ycor() < car.ycor() + 15):
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
