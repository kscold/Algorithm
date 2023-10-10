class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        def subsetSumEqualToK(index, nums, target):  # 인덱스, 배열, 타켓
            dp = [[False for i in range(target + 1)] for j in range(len(nums))]

            for i in range(index):  # base case
                dp[i][0] = True

            for i in range(1, len(nums)):
                for t in range(1, target + 1):
                    not_take = dp[i - 1][t]
                    take = False

                    if nums[i] <= t:
                        take = dp[i - 1][t - nums[i]]

                    dp[i][t] = take or not_take

            return dp[len(dp) - 1][len(dp[0]) - 1]

        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        desired_sum = total_sum // 2

        return subsetSumEqualToK(len(nums), nums, desired_sum)

nums = list(map(int, input().split()))

solution = Solution()
result = solution.canPartition(nums)
print(result)