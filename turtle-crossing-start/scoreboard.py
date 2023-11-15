from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.new_level = 0
        self.level_score()

    def level_score(self):
        self.penup()
        self.goto(-250, 250)
        self.color("black")
        self.new_level += 1
        self.write(f"LEVEL:{self.new_level}", font=FONT)
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER",align="center", font=FONT)
        self.hideturtle()