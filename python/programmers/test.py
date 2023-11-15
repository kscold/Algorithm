def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            print(stack)
            stack.pop()
            k -= 1

        stack.append(n)
    print(stack)

    # 아직 제거되지 못 한 숫자를 뒤에서 삭제
    if k > 0:
        print(stack[:-k])
        stack = stack[:-k]

    return ''.join(stack)


number = str(input())
k = int(input())
print(solution(number, k))


# 카운트의 배수

# 1924
#
# 1 2
#
# 1231234
#
# 11 2
#
#
# 775841
#
# 1 22 4