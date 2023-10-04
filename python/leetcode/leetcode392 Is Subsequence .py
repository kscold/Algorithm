class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s):
                return True

            if j == len(t):
                return False

            if s[i] == t[j]:
                memo[(i, j)] = dp(i + 1, j + 1)
                return dp(i + 1, j + 1)

            else:
                memo[(i, j)] = dp(i, j + 1)
                return dp(i, j + 1)

        return dp(0, 0)

s = str(input())
t = str(input())
solution = Solution()
subsequence = solution.isSubsequence(s, t)
print(subsequence)
