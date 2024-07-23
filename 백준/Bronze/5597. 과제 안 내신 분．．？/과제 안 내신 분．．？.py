import sys

input = sys.stdin.readline

datas = []
for _ in range(28):
    x = int(input())
    datas.append(x)

datas.sort()

for i in range(1, 31):
    if i in datas:
        continue
    else:
        print(i)
