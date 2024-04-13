n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0
        draw2 = 0

        for y in range(i, i + 8):
            for x in range(j, j + 8):
                if (y + x) % 2 == 0:
                    if board[y][x] != 'B':
                        draw1 += 1
                    if board[y][x] != 'W':
                        draw2 += 1
                else:
                    if board[y][x] != 'W':
                        draw1 += 1
                    if board[y][x] != 'B':
                        draw2 += 1
        result.append(draw1)
        result.append(draw2)

print(min((result)))
