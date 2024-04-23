import sys

input = sys.stdin.readline
num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = input().split()

answer = 0
for i, val in enumerate(n[::-1]):
    answer += int(b) ** i * num_list.index(val)
print(answer)
