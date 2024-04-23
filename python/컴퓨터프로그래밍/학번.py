# name = input("이름을 입력하세요")
# hak = int(input("학번을 입력하시오 입력) 230117 : "))
#
# entry_yy = hak // 10000
#
# major = hak % 10000 // 100
# print(major)
#
# bunho = hak % 10000 % 100
# print("입학년도" +  str(entry_yy) + "년")
#
# if major == 1:
#     print("전공 : 소프트웨어 ")
# elif major == 2:
#     print("전공 : 휴먼지능로봇공학 ")
#
# print("번호 = %02d" % (bunho))

# print("%2.4f" % (3.23432))
# print("%05d" % (3234)) # 5칸을 표현하는데 앞에 칸은 0을 붙임

# import turtle
#
# turtle.shape("turtle")
# turtle.penup()
#
# while True:
#     x = int(input("x위치 ==>"))
#     y = int(input("y위치 ==>"))
#     text = input("쓰고 싶은 글자 ==>")
#
#     turtle.goto(x, y)
#     turtle.write(text, font=("Arial", 30))
#
# turtle.done()

# import turtle
# import random
#
# turtle.shape("turtle")
# turtle.pensize()
# turtle.pencolor("blue")
# turtle.screensize(300, 300)
# turtle.setup(330, 330)
#
# while True:
#     angle = random.randint(0, 360)
#     distance = random.randint(10, 100)
#     turtle.right(angle)
#     turtle.forward(distance)
#
#     curX = turtle.xcor()
#     curY = turtle.ycor()
#
# if (curX >= -150 and curX <= 150) and (curY >= -150 and curY <= 150):
#     print("Good Boy~")
# else:
#     turtle.goto(0, 0)
#
# turtle.done()
