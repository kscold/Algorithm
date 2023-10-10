class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1) + 1 # 0번째 인덱스는 무시하기 위해서
        len2 = len(text2) + 1
        dp = [[0 for i in range(len2)] for j in range(len1)] # len1의 길이가 행의 갯수 len2의 길이가 열의 갯수


        for i in range(1, len1): # 1부터 n까지
            for j in range(1, len2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)
        return dp[len1 - 1][len2 - 1] # len의 길이를 1까지 줄어들게 만듬


text1 = str(input())
text2 = str(input())

solution = Solution()

result = solution.longestCommonSubsequence(text1, text2)
print(result)