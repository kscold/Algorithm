import sys

input = sys.stdin.readline

n = int(input())

datas = []
for i in range(n):
    datas.append(int(input()))

for data in sorted(datas):
    print(data)