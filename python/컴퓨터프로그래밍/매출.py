# import turtle
#
# turtle.shape("turtle")
# turtle.pensize(5)
# turtle.pencolor("blue")
#
# while True:
#     angle = int(input("거북이의 회전 각도 :"))
#     distance = int(input("거북이의 이동 거리 :"))
#
#     turtle.right(angle)
#     turtle.forward(distance)


import turtle

turtle.shape("turtle")
turtle.penup()


while True:
    x = int(input("x위치 ==>"))
    y = int(input("y위치 ==>"))
    text = input("쓰고 싶은 글자 ==>")

    turtle.goto(x,y)
    turtle.write(text, font=("Arial",30))

turtle.done()