from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()