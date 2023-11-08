class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def dfs(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()

        result = []
        dfs(0, [])
        return result


nums = list(map(int, input().split()))
solution = Solution()
result = solution.subsets(nums)
print(result)
