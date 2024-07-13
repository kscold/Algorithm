def solution(array):
    set_array = list(set(array))
    result = {}
    for item in set_array:
        result[item] = array.count(item)

    values_list = list(result.values())
    max_value = max(list(result.values()))
    key_list = list(result.keys())

    if values_list.count(max_value) > 1:
        answer = -1
    else:
       index = values_list.index(max_value)
       answer = key_list[index]

    return answer