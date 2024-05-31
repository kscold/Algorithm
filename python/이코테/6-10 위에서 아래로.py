# 입력
# 3
# 15
# 27
# 12

# 출력
# 27 15 12

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=" ")
