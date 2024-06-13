from turtle import Turtle
FONT = ("Courier", 24, "normal")
GAME_OVER = ("Courier", 30, "bold")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-225, 250)
        self.write("Level: ", align='center', font=FONT)
        self.goto(-165, 249)
        self.write(self.score, align='center', font=FONT)


    def player_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=GAME_OVER)

