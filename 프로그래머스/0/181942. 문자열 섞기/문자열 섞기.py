def solution(str1, str2):
    words = []

    i = 0
    while len(str1) > i:
        words.append(str1[i])
        words.append(str2[i])
        i += 1

    answer = "".join(words)

    return answer