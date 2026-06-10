from turtle import Turtle

class BrickManager:
    def __init__(self):
        self.bricks = []
        self.create_bricks()

    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        for row in range(5):
            for col in range(10):
                brick = Turtle()
                brick.shape("square")
                brick.color(colors[row])
                brick.penup()
                brick.goto(-350 + col * 70, 250 - row * 30)
                self.bricks.append(brick)