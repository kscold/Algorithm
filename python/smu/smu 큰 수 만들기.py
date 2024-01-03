# 큰 수 만들기
# 음수가 아닌 정수로 된 배열이 주어졌을 때 주어진 수를 붙여서 만들 수 있는 가장 큰 수를 구하시오. 반환되는 수는
# 문자열로 만들어져야 한다.

# 예시)
# 입력
# 2 // 총 2 개의 입력
# 2 10 2 // 2 개의 숫자, 10, 2
# 5 3 30 34 5 9 // 5 개의 숫자, 3, 30, 34, 5, 9

# 출력
# 210
# 9534330

# 라이브러리 사용
# from functools import cmp_to_key

# def compare(x, y):
#     # x와 y를 연결했을 때 더 큰 숫자를 만들 수 있는 순서로 정렬
#     return int(y + x) - int(x + y)
#
# def largest_number(nums):
#     # 문자열로 변환하여 정렬, 비교 함수를 사용하여 정렬
#     sorted_nums = sorted(map(str, nums), key=cmp_to_key(compare))
#
#     # 모든 수가 0인 경우에는 "0"을 반환
#     if sorted_nums[0] == "0":
#         return "0"
#
#     # 정렬된 숫자를 연결하여 문자열로 반환
#     return "".join(sorted_nums)
#
# # 입력
# n = int(input())
# data = []
# for _ in range(n):
#     data.append(list(map(int, input().split()[1:])))
#
# # 출력
# for numbers in data:
#     result = largest_number(numbers)
#     print(result)

def largest_number(nums):
    # 숫자를 문자열로 변환하여 정렬
    sorted_nums = sorted(map(str, nums), key=lambda x: x * 3, reverse=True)
    print(sorted_nums)

    # 모든 수가 0인 경우에는 "0"을 반환
    if sorted_nums[0] == "0":
        return "0"

    # 정렬된 숫자를 연결하여 문자열로 반환
    return "".join(sorted_nums)

# 입력
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split()[1:])))

# 출력
for numbers in data:
    result = largest_number(numbers)
    print(result)




# 2
# 2 10 2
# 5 3 30 34 5 9


