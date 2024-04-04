import random

n = int(input("반복할 횟수를 입력: "))

for i in range(n):
    my = input("유저: ")
    mylist = ["가위", "바위", "보"]
    com = random.choice(mylist)

    print(f"컴퓨터: {com}")

    if my == "가위" and com == "보":
        print("이겼습니다.")
    elif my == "바위" and com == "보":
        print("졌습니다.")
    elif my == "보" and com == "보":
        print("비겼습니다.")

    elif my == "바위" and com == "가위":
        print("이겼습니다.")
    elif my == "가위" and com == "가위":
        print("비겼습니다.")
    elif my == "보" and com == "가위":
        print("졌습니다.")


    elif my == "보" and com == "바위":
        print("이겼습니다.")
    elif my == "바위" and com == "바위":
        print("비겼습니다.")
    elif my == "가위" and com == "바위":
        print("졌습니다.")
