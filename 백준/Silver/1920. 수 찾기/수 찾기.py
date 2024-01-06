import sys

input = sys.stdin.readline

n = int(input())
data = set(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

for t in target:
    if t in data:
        print(1)
    else:
        print(0)