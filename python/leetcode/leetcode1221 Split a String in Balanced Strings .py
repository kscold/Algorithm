import sys

print("s = ", end='')
s = str(sys.stdin.readline().strip())

result = 0
r = 0
l = 0

for i in s:
    if i == "R":
        r += 1
    elif i == "L":
        l += 1

    if r == l:
        result += 1
        r = 0
        l = 0

print(result)
