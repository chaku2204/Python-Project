from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet", prompt="which color you want to take bet?Enter a color")

color = ["gold", "orange", "red", "maroon", "violet", "magenta"]
name = []

y = -180
for i in range(0,len(color)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[i])
    new_turtle.penup()
    y = y + 50
    new_turtle.goto(x=-230,y=y)
    name.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in name:
        if turtle.xcor() > 220:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win")
            else:
                print(f"{winning_color} win")
        a = random.randint(0,10)
        turtle.forward(a)


screen.exitonclick()