n = int(input())

data = []
for _ in range(n):
    data.append(int(input()))

memo = [0] * n
memo[0] = data[0]

if 1 < n:
    memo[1] = data[0] + data[1]
if 2 < n:
    memo[2] = max(memo[1], max(data[0], data[1]) + data[2])

for i in range(3, n):
    memo[i] = max(memo[i - 1], memo[i - 2] + data[i], memo[i - 3] + data[i - 1] + data[i])

print(memo[n - 1])