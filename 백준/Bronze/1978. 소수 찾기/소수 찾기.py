n = int(input())
datas = list(map(int, input().split()))
count = 0

for data in datas:
    if data == 1:
        continue

    for i in range(2, data):
        if data % i == 0:
            break
    else:
        count += 1
print(count)