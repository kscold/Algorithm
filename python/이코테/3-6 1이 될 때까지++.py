# 성능은 이전 보다 훨씬 좋으나 로직이 훨씬 복잡하고 떠오르기 하기 힘듬

n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k # n을 k로 나누었을 때 얻을 수 있는 가장 큰 k 배수
    result += (n - target) # n과 target 사이에 있는 나머지 값을 더하는 것, 1인 경우를 한번에 구할 수 있게 만들어줌
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)
print(result)
