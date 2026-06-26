from turtle import Turtle
from bricks import BrickManager
brick_manager = BrickManager()
FONT = ("Courier", 24, "normal")
t = Turtle()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.lives = 3
        self.life_stamps = []
        self.update_scoreboard()
        self.draw_lives()


    def draw_lives(self):
        t.clearstamps()
        self.life_stamps.clear()
        t.shape("circle")
        t.color("red")
        t.penup()
        for i in range(self.lives):
            t.goto(-300 + (i * 30), 280)
            stamp_id = t.stamp()
            self.life_stamps.append(stamp_id)
        if self.lives == 0:
            t.clearstamps()
            self.life_stamps.clear()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)
        
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()