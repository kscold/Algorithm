# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.
#
# 출력
# 첫째 줄에 N!을 출력한다.
#
# 예제 입력 1
# 10
# 예제 출력 1
# 3628800
# 예제 입력 2
# 0
# 예제 출력 2
# 1


def factorial(n):
    if n == 0:
        return 1

    if n == 1:
        memo[1] = 1

    if n in memo:
        return memo[n]

    memo[n] = n * factorial(n - 1)
    return memo[n]


n = int(input())
memo = [0] * (n + 1)
print(factorial(n))
