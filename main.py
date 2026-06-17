from turtle import Turtle, Screen
import random
cores = [(252, 251, 246), (253, 247, 251), (236, 251, 243), (200, 10, 35), (247, 236, 37), (240, 244, 251), (239, 231, 3), (36, 216, 77), (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18), (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7), (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218), (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161)]
timmy = Turtle()
timmy.shape("turtle")
omega = 1
screen = Screen()
screen.colormode(255)
timmy.speed('fastest')

timmy.penup()


for y in range(0, 50):
    for x in range (0, omega):
        timmy.dot(20, random.choice(cores))
        timmy.forward(40)
    timmy.left(90)
    omega += 1









screen.exitonclick()