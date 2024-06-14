from turtle import Turtle
FONT = ('Courier', 24, 'bold')
ALIGNMENT = 'center'


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("data.txt") as high_score:
            self.high_score = int(high_score.read())
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open('data.txt', 'w') as high_score:
                high_score.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    def keep_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()