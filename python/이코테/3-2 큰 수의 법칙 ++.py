 # 가장 큰 수가 K 번 반복되고 두번째로 큰 수가 1번 반복 되기 때문에 큰 수의 집합은 K+1이 된다.
 # 결과적으로 이 코드가 좀 더 최적화된 방법임 M이 엄청 클 때를 방지
import sys
 
n, m, k = map(int, sys.stdin.readline().split())
 
data = list(map(int, sys.stdin.readline().split()))
 
data.sort() # 오름차순으로 정렬
 
fisrt = data[n - 1] # 가장 큰수
second = data[n - 2] # 두번째로 큰 수

# 위의 아이디어를 적용하여
count = int(m / (k + 1)) * k # m 총 배열의 크기를 반복되는 집합 (K+1)로 나누고 k를 다시 곱해주면 가장 큰 수가 등장하는 횟수가 된다.
count += m % (k + 1) # 여기에 추가적으로 m이 (k+1)로 나누어 떨어지지 않을 때를 고려하기 위해 나머지 연산을 해준다.

result = 0
result += count * fisrt # 가장 큰 수가 등장하는 갯수 곱하기 가장 큰 수를 해서 가장큰 수의 총합을 구함
result += (m - count) * second # (m-count) 이 코드는 총 더하는 횟수 m에서 가장 큰 수가 등장하는 횟수를 빼주므로 두번째로 큰 수가 등장하는 횟수를 보여줌 여기에 두번째로 등장하는 횟수를 곱해서 총 두번째로 큰 수의 총합을 구함

print(result)
