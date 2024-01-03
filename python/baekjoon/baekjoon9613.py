# t = int(input())
#
# def gcd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)
#
# for _ in range(t):
#     n = list(map(int, input().split()))
#     ncount = len(n)
#     gcd_sum = 0
#
#     # 리스트의 모든 요소를 gcd의 파라터로 넣는 코드
#     for i in range(1, ncount):  # 두 수 사이의 GCD를 계산하므로 인덱스 범위를 수정
#         for j in range(i+1, ncount):  # 두 수 사이의 GCD를 계산하므로 인덱스 범위를 수정
#             gcd_sum += gcd(n[i], n[j])  # n[j]와 n[i]로 수정
#
#
#     print(gcd_sum)


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def calculate_total_gcd(arr):
    total_gcd_sum = 0
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            total_gcd_sum += gcd(arr[i], arr[j])

    return total_gcd_sum


t = int(input())
for _ in range(t):
    n = list(map(int, input().split()))
    result = calculate_total_gcd(n[1:])  # 첫 번째 원소는 수의 개수이므로 제외
    print(result)
