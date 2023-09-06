import sys

print("s = ", end='')
s = sys.stdin.readline()

count = 0
count_r = 0
count_l = 0
for i in s:
    if i == "L":
        count_l += 1
    elif i == "R":
        count_r += 1

    if count_l == count_r:
        count += 1
        count_l, count_r = 0, 0
print(count)
