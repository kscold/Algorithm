# class Solution(object):
#     def numsSameConsecDiff(self, n, k):
#         """
#         :type n: int
#         :type k: int
#         :rtype: List[int]
#         """
#         ans = []
#
#         def dfs(cur):
#             if len(cur) == n:
#                 if cur not in ans:
#                     ans.append(int(cur))
#                 if cur in ans:
#                     return
#
#             else:
#                 last = int(cur[-1])
#
#                 if last - k >= 0:
#                     dfs(cur + str(last - k))
#                 if k != 0 and last + k < 10:
#                     dfs(cur + str(last + k))
#
#         for i in range(1, 10):
#             dfs(str(i))
#
#         return ans

class Solution(object): # 백트래킹 풀이
    def numsSameConsecDiff(self, n, k): # n은 길이 k는 차이
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """

        results = []

        def backtrack(i, path):
            if i == n:
                results.append(path)
                return

            last_digit = path % 10

            if (k == 0):
                backtrack(i + 1, path * 10 + last_digit)
                return

            if (last_digit - k >= 0):
                backtrack(i + 1, path * 10 + last_digit - k)

            if (last_digit + k <= 9):
                backtrack(i + 1, path * 10 + last_digit + k)

        for i in range(1, 10):
            backtrack(1, i)

        return results


n, k = map(int, input().split())
solution = Solution()
result = solution.numsSameConsecDiff(n, k)
print(result)
