class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        result = 0
        empty_bottles = 0

        while numBottles > 0:
            # 현재 물병을 마심
            result += numBottles  # result = 15, result = 15 + 3
            # 빈 물병을 저장
            empty_bottles += numBottles  # empty_bottles = 15, empty_bottles = 15 + 3
            # 빈 물병을 교환해서 새로운 물병을 얻음
            numBottles = empty_bottles // numExchange  # numBottles = 3, numBottles = 4
            # 남은 빈 물병
            empty_bottles %= numExchange  # empty_bottles = 0, empty_bottles = 2

        return result


solution = Solution()
a, b = map(int, input().split())

result = solution.numWaterBottles(a, b)
print(result)
