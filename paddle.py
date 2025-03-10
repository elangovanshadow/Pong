
from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,a):
        super().__init__()
        self.create_paddle(a)


    def create_paddle(self, Position):

        self.penup()
        self.color('white')
        self.shape('square')
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(Position)

    def move_up(self):
        self.forward(40)


    def move_down(self):
        self.backward(40)
