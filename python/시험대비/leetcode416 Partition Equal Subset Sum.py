# class Solution(object):
#     def canPartition(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#
#         def subsetSumEqualToK(index, nums, target):  # 인덱스, 배열, 타켓
#             dp = [[False for i in range(target + 1)] for j in range(len(nums))]
#
#             for i in range(index):  # base case
#                 dp[i][0] = True # 첫번째 열을 전부 0으로 초기화
#
#             for i in range(1, len(nums)): # 1부터 리스트 요소 길이의 -1까지 반복
#                 for t in range(1, target + 1): # 1부터 target까지 반복
#                     not_take = dp[i - 1][t] # 현재 고려중인 i 번째 요소를 선택하지 않은 경우
#                     take = False # 현재 고려중인 i 번째 요소를 선택한 경우
#
#                     if nums[i] <= t:
#                         take = dp[i - 1][t - nums[i]]
#
#                     dp[i][t] = take or not_take
#
#             return dp[len(dp) - 1][len(dp[0]) - 1]
#
#         total_sum = sum(nums)
#
#         if total_sum % 2 == 1:
#             return False
#
#         desired_sum = total_sum // 2
#
#         return subsetSumEqualToK(len(nums), nums, desired_sum)
#

# 효율적인 풀이
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums) # 총합

        if total % 2 != 0: # 2로 나누어 떨어지지 않으면 두개의 부분집합으로 나눌 수 없음
            return False

        total //= 2 # 나누어 떨어질 수 있으면 절반을 total에 저장

        dp = [0] * 20001 # dp 테이블을 초기화
        dp[0] = 1 # dp[0] = 1을 대입

        for num in nums:
            idx = total # total를 idx 변수에 저장
            while idx - num >= 0: # idx에서 num을 뺀 값 총합의 중간에서 요소를 뺀 값이 음수일때까지 반복
                if dp[idx] or dp[idx - num]: # 만약 dp[idx] 나 dp[idx - num] 값이 있으면 dp[idx]에 1을 대입
                    dp[idx] = 1
                idx -= 1 # 인덱스를 하나 줄임

            if dp[total]: # dp의 total이 존재하면 True
                return True

        return False # 그렇지 않으면 False 반환


nums = list(map(int, input().split()))

solution = Solution()
result = solution.canPartition(nums)
print(result)