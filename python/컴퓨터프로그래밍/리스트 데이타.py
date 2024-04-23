datas = list(map(int, input().split()))
# 7 6 3 8 2

count = 0
for data in datas:
    if data >= 5:
        count += 1

print(f"5을 넘는 데이터 갯수:{count}")
print(sorted(datas))
