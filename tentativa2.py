from turtle import Turtle, Screen
import random
cores = [(236, 251, 243), (200, 10, 35), (247, 236, 37),
         (240, 244, 251), (239, 231, 3), (36, 216, 77), (223, 159, 61),
         (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152),
         (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7),
         (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218),
         (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161)]
timmy = Turtle()
timmy.shape("turtle")
screen = Screen()
screen.colormode(255)
logic_value = True
timmy.penup()
timmy.speed('fastest')


def turn_left(angle):
    timmy.left(angle)
    timmy.forward(50)
    timmy.left(angle)


def turn_right(angle):
    timmy.right(angle)
    timmy.forward(50)
    timmy.right(angle)


for y in range(0, 10):
    for x in range(0, 9):
        timmy.dot(20, random.choice(cores))
        timmy.forward(50)
        timmy.dot(20, random.choice(cores))
    if logic_value:
        turn_left(90)
        logic_value = False
    else:
        turn_right(90)
        logic_value = True


    
screen.exitonclick()
