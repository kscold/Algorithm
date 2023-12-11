# 내가 푼 풀이
# import random
#
#
# class Solution(object):
#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.nums = nums
#
#     def pick(self, target):
#         """
#         :type target: int
#         :rtype: int
#         """
#         # indices = [i for i, num in enumerate(self.nums) if num == target]
#         tmp = []
#         for t in target:
#             indices = []
#             for i, num in enumerate(self.nums):
#                 if num == t:
#                     indices.append(i)
#             if indices:
#                 tmp.append(random.choice(indices))
#
#         return tmp
#
#
# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.pick(target)
#
# nums = [1, 2, 3, 3, 3]
# target = [3, 1, 3]
#
# obj = Solution(nums)
# param_1 = obj.pick(target)
# print(param_1)


import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.idx = {}  # 빈 딕셔너리 선언
        for i, num in enumerate(nums):
            if num not in self.idx:  # 딕셔너리가 비었으면
                self.idx[num] = [i]  # 넘버 키 값에 인덱스를 넣음
            else:  # 딕셔너리가 안비었으면
                self.idx[num].append(i)  # 넙버 키 값 뒤에 인덱스를 추가함 3의 경우 딕셔너리에 {1 : 0, 2 : 1, 3 : [2, 3, 4]} 2 3 4 리스트로 들어감

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idx = self.idx[target] # 딕셔너리 키 3의 값 [2, 3, 4]를 뽑음
        return random.choice(idx) # [2, 3, 4] 중에서 랜덤 선택


# Your Solution object will be instantiated and called as such:

nums = [1, 2, 3, 3, 3]
target = 3
obj = Solution(nums)
param_1 = obj.pick(target)
print(param_1)
