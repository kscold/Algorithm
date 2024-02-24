import random_tets

n = int(input())
per = int(input())
want = 0
v = []

for _ in range(n):
    x, y = map(int, input().split())
    v.append((x, y))

if n == 1:
    print("possible")
    exit()

# n 점의 수 per 직선이 지나야하는 퍼센티지
# want는 최소한 지나가야 하는 점의 개수

if n * per % 100 == 0: # 퍼센트가 딱 떨어지는 경우
    want = n * per // 100
else: # 퍼센트가 딱 떨어지지 않는경우
    want = n * per // 100 + 1 # 예를 들어 5 * 30 // 100 = 1이지만, 지나가야 하는 최소 점의 개수는 1이 아닌 2가 되어야 한다. 따라서 want를 1 더해주어야 한다.
    # 왜 냐면 이 경우 실제는 1.5 이기 때문에 소수점 이해 갯수를 다루지 못하기에 올림을 하는 것이다.

def cnt(x, y): # 두 점 x, y를 지나는 직선이 몇 개의 점을 지나가는지 계산하는 함수
    ret = 0
    for i in v:
        ret += (y[1] - x[1]) * (i[0] - x[0]) == (i[1] - x[1]) * (y[0] - x[0])
    return ret

rd = random.Random((int((random.random() * 1000000000)) % 1000000000))

for _ in range(150):
    a = rd.randint(0, n-1)
    b = rd.randint(0, n-1)
    while a == b:
        b = rd.randint(0, n-1)
    if cnt(v[a], v[b]) >= want:
        print("possible")
        exit()

print("impossible")
