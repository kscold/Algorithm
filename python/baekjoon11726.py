import sys

n = int(sys.stdin.readline())

D = [0] * 1001

def dp(x):
    if x == 1:
        return 1 # 정상 종료 조건의 해당
    if x == 2:
        return 2
    if D[x] != 0: # 만약 D 배열이 0이 아니면 D[x]을 반환(스토어)
        return D[x]
    D[x] = (dp(x-1) + dp(x-2)) % 10007
    return D[x]


print(dp(n))