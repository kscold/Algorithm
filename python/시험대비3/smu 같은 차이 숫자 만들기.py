# 같은 차이 숫자 만들기
# 정수 n 과 k 가 주어진다. 다음 조건을 만족하는 모든 n 자리수 숫자를 만드는 함수를 작성하시오.
# 인접한 두 자리의 수의 차이가 정확히 k 이어야 한다.
# 0 이 앞에 나올 수 없다. 01, 0234 등은 허락되지 않음
# 작은 수에서 큰 수의 순서대로 출력한다.

# 예시)
# 입력
# 2 // 총 2 개의 입력
# 3 7 // 3 자리의 수, 차이가 7
# 2 1 // 2 자리의 수, 차이가 1

# 출력
# 181 292 707 818 929
# 10 12 21 23 32 34 43 45 54 56 65 67 76 78 87 89 98

def generate_numbers(n, k):
    result = []
    for num in range(10 ** (n - 1), 10 ** n):
        num_str = str(num)
        valid = True

        # 0이 앞에 나오는 경우는 제외
        if '0' in num_str:
            continue

        # 인접한 두 자리의 수의 차이가 정확히 k인지 확인
        for i in range(len(num_str) - 1):
            if abs(int(num_str[i]) - int(num_str[i + 1])) != k:
                valid = False
                break

        if valid:
            result.append(num_str)

    return result


# 입력
k = int(input())
n_values = []
for _ in range(k):
    n, m = map(int, input().split())
    n_values.append((n, m)) # 튜플 형태로 저장

# 출력
for n, m in n_values:
    result = generate_numbers(n, m)
    print(" ".join(result))

# 2
# 3 7
# 2 1
