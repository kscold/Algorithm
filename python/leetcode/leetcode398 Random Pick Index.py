import random


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.idx = {}
        for i, num in enumerate(nums):
            if num not in self.idx:
                self.idx[num] = [i]
            else:
                self.idx[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        idx = self.idx[target]
        return random.choice(idx)


nums = [1, 2, 3, 3, 3]
target_values = [[3], [1], [3]]

obj = Solution(nums)

result = []
for target in target_values:
    for i in target:
        param_1 = obj.pick(i)
        result.append(param_1)

print(result)
