class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        total_drinks = numBottles
        empty_bottles = numBottles

        while empty_bottles >= numExchange:
            new_drinks = empty_bottles // numExchange
            total_drinks += new_drinks

            remaining_bottles = empty_bottles % numExchange

            empty_bottles = new_drinks + remaining_bottles

        return total_drinks

numBottles, numExchange = map(int, input().split())
solution = Solution()
result = solution.numWaterBottles(numBottles, numExchange)
print(result)
