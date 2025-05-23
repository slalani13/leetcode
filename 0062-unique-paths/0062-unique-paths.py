class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n] * m

        for i in range(n):
            dp[0][i] = 1
        
        for j in range(m):
            dp[j][0] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                print(i, j)
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

