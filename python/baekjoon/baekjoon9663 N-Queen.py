# 퀸은 같은 행 같은 형 같은 대각선으로 움직인다.

# 기본 가정: 같은 행에는 퀸을 놓지 않는다.
# 유망 함수 구현: 같은 열이나 같은 대각선에 놓는지를 확인
# 파이썬이 너무 느려 통과가 안되므로 pypy로 통과해야함

def n_queens(col, i):
    n = len(col) - 1
    count = 0

    if promsing(col, i):
        if i == n:
            return 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                count += n_queens(col, i + 1)

    return count


def promsing(col, i):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
        k += 1
    return flag


n = int(input())
col = [0] * (n + 1)
result = n_queens(col, 0)
print(result)
