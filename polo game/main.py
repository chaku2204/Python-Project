import time
from turtle import Screen
from paddle import padle
from ball import Ball_move
from scoreboard import Score_board
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.tracer(0)


r_paddle = padle((350,0))
l_paddle = padle((-350,0))


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

ball= Ball_move()
Score = Score_board()
t = 0.1
while True:
   screen.update()
   time.sleep(t)
   ball.ball_mov()


   if ball.ycor() > 280 or ball.ycor() < -280:
      ball.bounce()

   if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
      ball.collison()
      t*=0.9

   if ball.xcor() > 370:
         ball.reset_positin()
         Score.lscore()
         t = 0.1


   if ball.xcor() < -370:
          ball.reset_positin()
          Score.rscore()
          t = 0.1


screen.exitonclick()