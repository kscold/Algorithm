def solution(num_list):
    string_odd = ""
    string_even = ""
    for num in num_list:
        if num % 2 == 0:
            string_even += str(num)
        else:
            string_odd += str(num)
    
    answer = int(string_odd) + int(string_even)
    return answer