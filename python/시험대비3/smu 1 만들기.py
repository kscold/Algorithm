# 양의 정수 n 이 주어진다. 다음과 같은 연산을 취하면서 최종적으로 1 을 만들고자 한다.
# n 이 짝수이면 n <- n/2 연산 수행
# n 이 홀수이면, n <- n+1 연산 혹은 n <- n-1 연산 수행
# 1 을 만들기 위한 최소의 연산 수를 구하시는 함수를 작성하시오.
from sympy.strategies.core import switch

# 예시)
# 입력
# 2 // 총 2 개의 입력
# 8
# 34

# 출력
# 3
# 6


# 내가 푼 풀이
k = int(input())
n = []
for _ in range(k):
    n.append(int(input()))

tmp = []
for i in n:
    count = 0  # 각 정수에 대한 연산 횟수를 초기화
    while i != 1:
        if i % 2 == 0:
            i = i // 2
        else:
            i = i - 1
        count += 1  # 연산은 마지막에 한번만 하면 됨
    tmp.append(count)

for t in tmp:
    print(t)

# def min_operations_to_one(k, n):
#     result = []
#     for i in range(k):
#         count = 0
#         while n[i] != 1:
#             if n[i] % 2 == 0:
#                 n[i] //= 2
#             else:
#                 n[i] -= 1
#             count += 1
#         result.append(count)
#     return result
#
#
# # 입력
# k = int(input())  # 반복 횟수 입력
# n = []
# for _ in range(k):
#     n.append(int(input()))  # n = [8, 34]
#
# # 결과 출력
# result = min_operations_to_one(k, n)
# for r in result:
#     print(r)
