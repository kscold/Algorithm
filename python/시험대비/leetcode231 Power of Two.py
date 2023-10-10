# 리커시브로 풀은 문제
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n == 1:
#             return True
#
#         elif n % 2 != 0 or n == 0:
#             return False
#
#         return self.isPowerOfTwo(n // 2)
#
# n = int(input())
#
# solution = Solution()
# result = solution.isPowerOfTwo(n)
# print(result)

# DP로 풀은 문제 바텀업 방식 -> 그러나 메모리 초과 오류가 남
# class Solution(object):
#     def isPowerOfTwo(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n <= 0:
#             return False
#
#         dp = [False] * (n+1)
#         dp[1] = True
#
#         for i in range(2, n + 1):
#             if i % 2 == 0 and dp[i // 2]:
#                 dp[i] = True
#         return dp[n]
#
# n = int(input())
#
# solution = Solution()
# result = solution.isPowerOfTwo(n)
# print(result)

# DP로 풀은 문제 탑다운 방식
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]

            if n == 1:
                memo[n] = True
                return memo[n]

            elif n % 2 != 0 or n == 0:
                memo[n] = False
                return memo[n]

            return dp(n // 2)
        return dp(n)

n = int(input())

solution = Solution()
result = solution.isPowerOfTwo(n)
print(result)