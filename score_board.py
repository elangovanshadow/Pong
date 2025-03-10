from turtle import Turtle



class Score_Board(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Comic Sans MS", 50, "normal"))
        self.goto(100,200)
        self.write(self.r_score, align='center', font=("Comic Sans MS", 50, "normal"))



    def display(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=("Comic Sans MS", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=("Comic Sans MS", 50, "normal"))