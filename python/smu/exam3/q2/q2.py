import time


def q2(R, coords):
    # your code is here
    # ----------------------------------------------

    # coords는 x y 좌표 튜플

    import random
    import math

    circle_x = []
    circle_y = []

    # print(coords)
    for x, y in coords:
        circle_x.append(x)
        circle_y.append(y)

    # print(circle_x)
    # x, y = coords
    # print(x)

    # random angle
    alpha = 2 * math.pi * random.random()
    # random radius
    # r = R * math.sqrt(random.random())
    # calculating coordinates

    count = 0
    # print(tmp)
    for circle_x, circle_y in coords:
        # for one_x in circle_x:
        x = R * math.cos(alpha) + circle_x
        y = R * math.sin(alpha) + circle_y

        if 0 <= x <= 1000 and 0 <= y <= 1000:
            count += 1

    return count

    # import random
    # import math
    # def polynomial(R):
    #     return 2 * math.pi * R
    #
    # def find_maximum_value(N=100000):
    #     # 초기값 설정
    #     x_max = random.uniform(0, 1000)
    #     y_max = random.uniform(0, 1000)
    #     # y_max = polynomial(x_max)
    #
    #     # randomization 기법
    #     for _ in range(N):
    #         x_candidate = random.uniform(-10, 10)  # -10 이상 10 미만의 범위에서 무작위로 선택된 소수를 반환
    #         y_candidate = polynomial(R)
    #
    #         count = 0
    #         # 현재까지의 최대값보다 큰 값이 나오면 업데이트
    #         if y_candidate > y_max:
    #             # x_max, y_max = x_candidate, y_candidate
    #             count += 1
    #
    #     return count
    #
    # # 최대값 찾기
    # result = find_maximum_value()
    #
    # return result
    #

    # 결과 출력
    # print(f"다항식의 최대값: y = {y_max} (x = {x_max})")

    import random
    points = 10000

    circle_x = []
    circle_y = []

    count = 0
    for jj in range(points):
        for x, y in coords:
            circle_x.append(x)
            circle_y.append(y)

            for xx, yy in zip(circle_x, circle_y):
                if xx * xx + yy * yy < R:
                    count += 1
                print(count)
    # ----------------------------------------------
    return -1


def compare_output(file1, file2):
    f1 = open(file1, "r")
    f2 = open(file2, "r")

    lines1 = f1.readlines()
    lines2 = f2.readlines()

    success = True
    i = 0
    for _ in lines2:
        if lines1[i].strip() != lines2[i].strip():
            print("[%i] Wrong answer: Yours=\'%s\', Expected=\'%s\'\n" % (i + 1, lines1[i].strip(), lines2[i].strip()))
            success = False
            break
        i = i + 1

    if success:
        print("Success!")
    f1.close()
    f2.close()


# main code
input = open("input.txt", "r")  # input data
output = open("output.txt", "w")  # your answer

start_time = time.time()
line = input.readline().split()
R = int(line[0])
N = int(line[1])
coords = []
for _ in range(N):
    line = input.readline().split()
    x = int(line[0])
    y = int(line[1])
    coords.append((x, y))
result = q2(R, coords)
print(result)
output.write('{}\n'.format(result))

end_time = time.time()
## -----------------------------------------------

# DO NOT EDIT. Checking answers
input.close()
output.close()
compare_output("output.txt", "expected.txt")
print('Elapsed time: {:.2f} seconds. '.format(end_time - start_time), end='')
