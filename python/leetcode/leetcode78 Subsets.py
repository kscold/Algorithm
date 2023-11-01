# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # graph ={0:0}
#         visited = [0] * (len(nums) + 1)
#         ans = []
#
#         # for num in nums:
#         #     u = num
#         #     if u not in graph:
#         #         graph[u] = []
#
#         #     graph[u].append(u)
#
#         def dfs(v):
#             if v == len(nums) + 1:
#                 for i in range(1, len(nums) + 1):
#                     if visited[i] == 1:
#                         ans.append(i)
#             else:
#                 ans[v] = 1
#                 dfs(v + 1)
#                 ans[v] = 0
#                 dfs(v + 1)
#
#         dfs(1)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        li = []
        idx = 0
        ans = []

        def subsets(nums, li, idx):
            if idx == n:
                temp = []
                for i in li:
                    temp.append(i)
                ans.append(temp)
                return

            li.append(nums[idx])
            subsets(nums, li, idx + 1)
            li.pop()

            subsets(nums, li, idx + 1)

        subsets(nums, li, idx)

        return ans


solution = Solution()
result = solution.subsets([1, 2, 3])
print(result)
