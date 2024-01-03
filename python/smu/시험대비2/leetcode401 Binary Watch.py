class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        time = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        ans = []

        def dfs(start, k, hours, mins):
            if hours >= 12 or mins > 59:
                return

            if k == turnedOn:
                ans.append("%d:%02d" % (hours, mins))
                return

            for i in range(start, 10):
                if i < 4:
                    dfs(i + 1, k + 1, hours + time[i], mins)
                else:
                    dfs(i + 1, k + 1, hours, mins + time[i])

        dfs(0, 0, 0, 0)
        return ans

turnedOn = int(input())
solution = Solution()
result = solution.readBinaryWatch(turnedOn)
print(result)