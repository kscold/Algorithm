datas = []
n = 1

while n <= 100:
    if n % 3 == 0:
        datas.append(n)

    n += 1

for data in datas:
    print(data, end=" ")

print()
print(f"총: {len(datas)}")
