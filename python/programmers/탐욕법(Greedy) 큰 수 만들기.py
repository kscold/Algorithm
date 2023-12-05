def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1

        stack.append(n)

    if k > 0: # 보통의 케이스에서는 필요가 없으나 예를 들어 54321의 경우 위의 while 조건문에서 한번도 걸리지 않으므로 이 경우 54 가 제일 큰 경우 이므로 54를 반환한다.
        stack = stack[:-k]

    return ''.join(stack)


n = str(input())
k = int(input())
result = solution(n, k)
print(result)
