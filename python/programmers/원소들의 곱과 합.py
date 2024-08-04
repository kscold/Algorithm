def solution(num_list):
    mul = 1
    square = 0
    for num in num_list:
        mul *= num
        square += num
    square = square ** 2
    answer = 0
    if mul < square:
        answer = 0
    elif mul > square:
        answer = 1

    return answer


print(solution([3, 4, 5, 2, 1]))
