from turtle import Turtle

class BrickManager:
    def __init__(self):
        self.bricks = []


    def create_bricks(self):
        colors = ["red", "orange", "yellow", "green", "blue"]
        for row in range(len(colors)):
            for col in range(11):
                brick = Turtle()
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.speed(0)
                brick.shape("square")
                brick.color(colors[row-1])
                brick.penup()
                brick.goto(-350 + col * 70, 250 - row * 30)
                self.bricks.append(brick)
        
            
            