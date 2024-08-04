def solution(a, d, included):
    # 3 7 11 15 19
    # i = 1
    # a + (i - 1) * d
    list_len = len(included)

    results = []
    for i in range(1, list_len + 1):
        if included[i - 1] == True:
            results.append(a + (i - 1) * d)

    answer = sum(results)
    return answer


print(solution(3, 4, [True, False, False, True, True]))
