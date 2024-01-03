import sys

print("jewel =", end = " ")
jewels = sys.stdin.readline().rstrip()
print("stones =", end = " ")
stones = sys.stdin.readline().rstrip()

count = 0

for stone in stones:
    for jewel in jewels:
        if stone == jewel:
            count += 1
        else:
            continue

print(count)