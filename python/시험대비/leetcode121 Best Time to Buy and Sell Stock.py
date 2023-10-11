class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        priceidx = len(prices)
        if priceidx == 0: # 인덱스 길이가 0 이면 값이 없으므로 0을 반환
            return 0

        dp = [0] * (priceidx + 1)

        min_price = prices[0] # 배열 첫번째 요소로 초기화
        max_diff = 0

        for i in range(1, priceidx): # 0을 초기화했으므로 1부터
            min_price = min(min_price, prices[i]) # 최솟값을 찾음
            max_diff = max(max_diff, prices[i] - min_price) # 최솟값을
            dp[i + 1] = max_diff # 마지막 dp 배열에 최대차이를 저장하기 위해

        return dp[len(prices)] # dp의 마지막 배열이 최대차이를 저장함


n = list(map(int, input().split()))
solution = Solution()
result = solution.maxProfit(n)
print(result)