n = int(input())
canvas = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1

black_area = sum(row.count(1) for row in canvas)

print(black_area)