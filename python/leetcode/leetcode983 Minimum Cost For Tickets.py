class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        d = [0 for _ in range(0, days[-1] + 1)]
        k = 0

        for i in range(1, days[-1] + 1):
            if i != days[k]:
                d[i] = d[i - 1]
            else:
                k += 1
                d[i] = min(
                    d[max(0, i - 1)] + costs[0],
                    d[max(0, i - 7)] + costs[1],
                    d[max(0, i - 30)] + costs[2]
                )

        return d[-1]

days = list(map(int, input().split()))
costs = list(map(int, input().split()))
solution = Solution()
result = solution.mincostTickets(days, costs)
print(result)
