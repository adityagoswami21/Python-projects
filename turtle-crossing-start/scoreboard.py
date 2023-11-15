from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.new_level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.color("black")
        self.level_score()

    def level_score(self):
        self.clear()
        self.write(f"LEVEL:{self.new_level}", font=FONT)

    def inc_level(self):
        self.new_level += 1
        self.level_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center", font=FONT)
        self.hideturtle()