# 입력
# 2
# 홍길동 95
# 이순신 77

# 출력
# 이순신 홍길동

# 내 풀이
# n = int(input())
#
# dic = {}
# for i in range(n):
#     key, value = map(str, input().split())
#     dic[key] = value
#
# result = sorted(dic)
#
# for i in result:
#     print(i, end=' ')

# 책 풀이
n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]))) # 점수, 이름으로 묶기 위해 튜플로 저장시킴

array = sorted(array, key=lambda student: student[1])

for student in array:
    print(student[0],end=' ')