def solution(num_list):
    if num_list[-1] > num_list[-2]:
        new_num = num_list[-1] - num_list[-2]
        num_list.append(new_num)
    else:
        new_num = num_list[-1] * 2
        num_list.append(new_num)

    return num_list


print(solution([2, 1, 6]))
