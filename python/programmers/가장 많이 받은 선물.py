# def solution(friends, gifts):
#     given_count = {friend: 0 for friend in friends}
#     received_count = {friend: 0 for friend in friends}
#     gift_index = {friend: 0 for friend in friends}
#     next_month_gifts = {friend: 0 for friend in friends}
#
#     for gift in gifts:  # ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
#         giver, receiver = map(str, gift.split())  # "muzi" "frodo"
#         given_count[giver] += 1
#         received_count[receiver] += 1
#
#     for friend in friends:
#         gift_index[friend] = given_count[friend] - received_count[friend]
#
#     for gift in gifts:
#         giver, receiver = gift.split()
#         if given_count[giver] > received_count[giver]:  # 준게 받은 것보다 많은 경우
#             next_month_gifts[receiver] += 1
#         elif given_count[giver] < received_count[receiver]:  # 받은게 준 것보다 많은 경우
#             next_month_gifts[giver] += 1
#         elif gift_index[giver] > gift_index[receiver]:
#             next_month_gifts[receiver] += 1
#         elif gift_index[giver] < gift_index[receiver]:
#             next_month_gifts[giver] += 1
#
#     answer = max(next_month_gifts.values())
#
#     return answer
#
#
# print(solution(["muzi", "ryan", "frodo", "neo"],
#                ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan",
#                 "neo muzi"]))

# 구현 문제 못풀었음 나중에 다시 풀어봐야함