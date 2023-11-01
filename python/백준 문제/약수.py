# 내 풀이
n = int(input())

k = list(map(int, input().split()))
k.sort()
first = k[0]
last = k[-1]
result = first * last

print(result)
