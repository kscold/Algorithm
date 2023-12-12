# 다항식의 최대값 찾기
# 다음 다항식 함수의 최대값을 randomization (무작위화) 기법을 이용해서 구하시오.
# 𝑦 = −𝑥^6 + 𝑥^4 + 7𝑥^3 + 9𝑥^2 − 10𝑥 − 1
# 𝑥 값은 -10 에서 10 을 벗어나지 않는다.
# 최대값은 소수점 4 자리까지 구하시오.

import random

# 다항식 정의
def polynomial(x):
    return -x ** 6 + x ** 4 + 7 * x ** 3 + 9 * x ** 2 - 10 * x - 1

def find_maximum_value(iterations=100000):
    # 초기값 설정
    x_max = random.uniform(-10, 10)
    y_max = polynomial(x_max)

    # randomization 기법
    for _ in range(iterations):
        x_candidate = random.uniform(-10, 10) # -10 이상 10 미만의 범위에서 무작위로 선택된 소수를 반환
        y_candidate = polynomial(x_candidate)

        # 현재까지의 최대값보다 큰 값이 나오면 업데이트
        if y_candidate > y_max:
            x_max, y_max = x_candidate, y_candidate

    return round(x_max, 4), round(y_max, 4) # x_max와 y_max 값을 각각 소수점 이하 4자리까지 반올림하여 반환


# 최대값 찾기
x_max, y_max = find_maximum_value()

# 결과 출력
print(f"다항식의 최대값: y = {y_max} (x = {x_max})")
