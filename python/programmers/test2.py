# people	        limit	return
# [70, 50, 80, 50]	100	    3
# [70, 80, 50]	    100	    3

# def solution(people, limit):
#     answer = 0
#     answer_list = []
#
#     def combi(n, ans):
#         if n == len(people):
#             temp = [i for i in ans]
#             answer_list.append(temp)
#             return
#         ans.append(people[n])
#         combi(n + 1, ans)
#         ans.pop()
#         combi(n + 1, ans)
#
#     combi(0, [])
#     print(answer_list)
#
#     items = list(set([tuple(set(item)) for item in answer_list]))
#     items = [v for v in items if v]
#     print(items)
#
#     # answer_list = set(answer_list)
#
#     for list_one in items:
#         if sum(list_one) <= limit:
#             print(list_one)
#             answer += 1
#     # for per in people:
#     #     if per == limit
#     return answer

def solution(people, limit):
    answer = 0
    start = 0
    end = people[-1]

    people = people.sort()

    while start != end:
        if people[start] + people[end] > limit:
            continue
        end -= 1
        answer += 1

    return answer

people = list(map(int, input().split()))
limit = int(input())
print(solution(people, limit))

# nums = [1, 2, 3, 4, 5]
#
# answer_list = []
#
# def combi(n, ans):
#     if n == len(nums):
#         temp = [i for i in ans]
#         answer_list.append(temp)
#         return
#     ans.append(nums[n])
#     combi(n + 1, ans)
#     ans.pop()
#     combi(n + 1, ans)
#
# combi(0, [])
# print(answer_list)
