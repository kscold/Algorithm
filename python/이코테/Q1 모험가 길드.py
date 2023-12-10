# n = int(input())
# l = list(map(int, input().split()))
#
# l.sort()
# tmp = l  # 1 2 2 2 3
# count = 0
# # i 0 1 2 3 4
# for i, data in enumerate(l):
#     if i + 1 == data:
#         count += 1
#
# print(count)

# 모범 답안
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)