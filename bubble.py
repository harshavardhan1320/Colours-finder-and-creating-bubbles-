import turtle
import random
from turtle import Screen
turtle.colormode(255)


t = turtle.Turtle()
R = random.Random()


t.hideturtle()
color = [(105, 80, 120), (168, 152, 177), (166, 155, 182), (100, 82, 122), (51, 28, 66)]
clr = (R.choice(color))


def forward_dots():
    t.pendown()
    t.dot(25, clr)
    t.penup()
    t.forward(50)



t.penup()
t.setx(-250)
t.sety(-200)



for _ in range(10):
    for x in range(10):
        clr = (R.choice(color))
        forward_dots()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.left(90)



screen = Screen()
screen.exitonclick()


