from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 260)

    def wrote(self):
        self.clear()
        self.write(f"Level : {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)