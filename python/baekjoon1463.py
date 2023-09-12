# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지이다.
# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
# 이 문제의 경우 그리디 알고리즘으로 풀 수 없는 문제임

import sys

N = int(sys.stdin.readline())

count = 0

while N != 1:
    if N % 3 == 0:
        N /= 3
        count += 1

    elif N % 2 == 0:
        N /= 2
        count += 1

    elif N % 3 and N % 2 != 0:
        N -= 1
        count += 1

print(count)