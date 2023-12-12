import sys; 
input = sys.stdin.readline
from math import ceil
from time import time
from random import randint

def ccw(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])

n = int(input())
if n <= 2:
    print('possible')
    exit()

p = int(input())
m = ceil(n * p * 0.01)
if m <= 2:
    print('possible')
    exit()

points = [tuple(map(int, input().split())) for _ in range(n)]

st = time()
while True:
    ends = []
    for _ in range(2):
        while True:
            p = points[randint(0, n - 1)]
            if p not in ends:
                ends.append(p)
                break
    result = 0
    for i in range(n):
        if not ccw(ends[0], ends[1], points[i]):
            result += 1
            if result == m:
                break
    if result == m:
        print('possible')
        break
    if time() - st > 10:
        print('impossible')
        break