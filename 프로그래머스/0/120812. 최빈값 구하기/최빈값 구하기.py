def solution(array):
    set_list = list(set(array))
    count_dict = dict()
    for key in set_list:
        count_dict[key] = array.count(key)

    keys_list = list(count_dict.keys())
    values_list = list(count_dict.values())
    max_value = max(values_list)

    if values_list.count(max_value) > 1:
        answer = -1
    else:
        index = values_list.index(max_value)
        answer = keys_list[index]

    return answer
