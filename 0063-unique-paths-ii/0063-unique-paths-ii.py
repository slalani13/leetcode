class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # subproblem - for any problem (r, c) the robot can go down to (r+1, c) or to the right to (r, c+1). Solve for these two problems and add them
        # recursive relation - unique(r, c) = unique(r+1, c) + unique(r, c+1)
        # topological order - going from m-1, n-1 to 0, 0
        # base case: m-1 row and n-1 col are 1 unless there is a obstacle in which case any space before the obstacle will be 0. Any space with an obstacle outside of that will also be 0.
        # original problem - unique(0, 0)
        # time - O(m*n)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        dp[m-1][n-1] = 1
        paths = 1
        # filter the last column i, n-1 
        for i in range(m-2, -1, -1):
            if obstacleGrid[i][n-1] == 1:
                paths = 0
            dp[i][n-1] = paths
        # filter the last row m-1, i
        paths = 1
        for i in range(n-2, -1, -1):
            if obstacleGrid[m-1][i] == 1:
                paths = 0
            dp[m-1][i] = paths
        
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:
                    dp[r][c] = dp[r+1][c] + dp[r][c+1]
        return dp[0][0]