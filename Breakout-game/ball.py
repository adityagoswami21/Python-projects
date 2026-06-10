from turtle import Turtle

class Ball(Turtle):
    # Initialize ball properties for breakout game
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.move_speed = 0.1
        self.dx = 10  # Change in x (horizontal movement)
        self.dy = 10  # Change in y (vertical movement)

    # Move the ball based on its current direction
    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    # Bounce the ball off the top wall
    def bounce_y(self):
        self.dy *= -1

    # Bounce the ball off the left and right walls
    def bounce_x(self):
        self.dx *= -1
    
    # Reset the ball on the paddle after it goes out of bounds
    def reset_position(self, position):
        self.goto(position)
        self.move_speed = 0.1
        self.dx = 10
        self.dy = 10