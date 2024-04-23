# 2중 for문 풀이
for i in range(5):
    for j in range(5):
        if i == j:
            print("1", end=" ")
        else:
            print("*", end=" ")
    print()

for i in range(5):
    print(i * "* ", end="")
    print(f"1 ", end="")
    print((4 - i) * "* ")

# 2중 for문 풀이
h = 0
for i in range(3):
    for j in range(1, i + 1):
        h = h + j
        print("%2d" % j, end="")

    for k in range(10, i, -1):
        print(" ", end="")
    print("%2d" % h, "\n")
    h = 0

for i in range(3):
    datas = list(map(int, input().split()))
    for data in datas:
        print(data, end=" ")
    print(sum(datas))
