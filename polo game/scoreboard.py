from turtle import Turtle

class Score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.read_score()

    def read_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"Left Score : {self.l_score}", align="center", font=("Arial", 20, "normal"))
        self.goto(100, 260)
        self.write(f"Right Score : {self.r_score}", align="center", font=("Arial", 20, "normal"))

    def lscore(self):
        self.l_score+=1
        self.read_score()

    def rscore(self):
        self.r_score+=1
        self.read_score()
