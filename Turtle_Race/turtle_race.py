from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_loc = -100
all_turtles = []

for turtle_count in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_count])
    new_turtle.penup()
    new_turtle.goto(-230, y_loc)
    y_loc += 40
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won.")
            else:
                print(f"You've lost... The {winning_color} turtle won.")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()
