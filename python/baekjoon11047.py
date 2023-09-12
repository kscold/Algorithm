# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
import sys

N, K = map(int, sys.stdin.readline().split())

coin_type = [0] * N

for i in range(len(coin_type)):
     coin_type[i] = int(sys.stdin.readline())

coin_type.sort(reverse = True)

count = 0

for coin in coin_type:
    if coin <= K:
        count += int(K / coin)
        K = K % coin
    else:
        continue

print(count)