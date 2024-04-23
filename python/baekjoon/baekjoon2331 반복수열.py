a, p = map(int, input().split())

data = [a]

while True:
    next = 0
    for i in str(data[-1]):
        next += int(i) ** p

    if next in data:
        break

    data.append(next)

print(data.index(next))
