def solution(code):
    end_index = len(code)
    ret = []
    mode = 0
    for i in range(end_index):  # "abc1abc1abc"
        if mode == 0:
            if code[i] != "1":
                if i % 2 == 0:
                    ret.append(code[i])
                else:
                    continue
            else:
                mode = 1
        else:
            if code[i] != "1":
                if i % 2 == 1:
                    ret.append(code[i])
                else:
                    continue
            else:
                mode = 0

    if not ret:
        answer = "EMPTY"
    else:
        answer = "".join(ret)

    return answer