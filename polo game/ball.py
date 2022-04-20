from turtle import Turtle

class Ball_move(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10

    def ball_mov(self):
        new_x = self.xcor() + self.x
        new_Y = self.ycor() + self.y
        self.goto(new_x,new_Y)

    def bounce(self):
        self.y *= -1

    def collison(self):
        self.x *=-1

    def reset_positin(self):
        self.goto(0,0)
        self.collison()
