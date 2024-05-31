# 문제
# 정수가 주어지면, 그 수의 정수 제곱근을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 n이 주어진다. (0 ≤ n < 263)

# 출력
# 첫째 줄에 q2 ≥ n인 가장 작은 음이 아닌 정수 q를 출력한다.

# 예제 입력 1
# 122333444455555
# 예제 출력 1
# 11060446

n = int(input()) # n은 현재 q**2 상태

start = 0
end = n

while start <= end:
    mid = (start + end) // 2

    if mid ** 2 < n:
        start = mid + 1
    elif mid ** 2 >= n:
        end = mid - 1


print(start)
