import sys

input = sys.stdin.readline

n, k = map(int, input().split())
levels = [int(input()) for _ in range(n)]

levels.sort()
start = levels[0]  
end = start + k 

res = 0
while (start <= end):
    mid = (start + end) // 2

    diff_sum = 0
    for level in levels:
        if mid > level:  
            diff_sum += (mid - level)

    if diff_sum <= k: 
        start = mid + 1
        res = max(mid, res)
    else:  
        end = mid - 1

print(res)
