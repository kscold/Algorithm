class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = []
        sub = []

        def dfs(i):
            if i >= len(nums):
                v = 0
                for i in sub:
                    v ^= i
                res.append(v)
                return

            sub.append(nums[i])
            dfs(i + 1)
            sub.pop()
            dfs(i + 1)

        dfs(0)
        return sum(res)

nums = list(map(int, input().split()))
solution = Solution()
result = solution.subsetXORSum(nums)
print(result)