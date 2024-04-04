from random import *
import turtle as t

t.shape("turtle")
t.pensize(5)
t.pencolor("blue")

t.screensize(300, 300)
t.setup(330, 330)

while True:
    angle = randint(0, 360)
    distance = randint(10, 100)
    t.right(angle)
    t.forward(distance)
    curX = t.xcor()
    curY = t.xcor()
    if (curX >= -150 and curX <= 150) and (curY >= -150 and curY <= 150):
        print("Good Boy")
    else:
        t.goto(0, 0)
t.done()
