def solution(a, d, included):
    list_len = len(included)

    results = []
    for i in range(1, list_len + 1):
        if included[i - 1] == True:
            results.append(a + (i - 1) * d)

    answer = sum(results)
    return answer