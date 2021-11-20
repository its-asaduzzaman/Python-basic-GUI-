import turtle
from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
timmy.shape('arrow')
timmy.color('red')
timmy.pensize(1)
timmy.speed('fastest')
'''write a dot line with color change'''
for _ in range(25):
    timmy.forward(10)
    timmy.color('white')
    timmy.forward(10)
    timmy.color('black')
'''write a dot line'''
for _ in range(25):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
'''draw different type of shape '''
color_list = ['orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'green','black']
shape = 3
move = 3
for i in range(8):
    for _ in range(move):
        timmy.forward(100)
        timmy.right(360 / shape)
    timmy.color(color_list[i])
    shape += 1
    move += 1

'''Random move '''
angle_list = [90, 180, 270, 360]
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)


def timmy_random_move(degree):
    timmy.forward(20)
    timmy.left(degree)
    print(random_color())
    random_color()


for _ in range(100):
    timmy_random_move(random.choice(angle_list))

'''Draw a circle'''
t.colormode(255)
screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)


def draw_spirograph(size_of_graph):
    for _ in range(int(360 / size_of_graph)):
        random_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_graph)


draw_spirograph(5)

'''bug with draw a circle'''
def draw_circle():
    screen.tracer(False)
    for _ in range(360):
        timmy.forward(2)
        timmy.left(1)
    screen.tracer(True)


for _ in range(80):
    draw_circle()
    random_color()
    timmy.right(5)
screen = Screen()
screen.exitonclick()
