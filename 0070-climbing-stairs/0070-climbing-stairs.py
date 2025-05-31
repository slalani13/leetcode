class Solution:
    def climbStairs(self, n: int) -> int:
        # SRTBOT
        # Subproblems -> How many steps does it take to reach n-1 steps?
        # Recursive relation -> F(n) = F(n-2) + F(n-1)
        # Topology - linear use for loop suffix[i:]
        # Base case - how many distinct ways can you climb 0 steps? 1 step? 2 steps? 0, 1, 2
        # Original problem - how many ways can you climb n steps?
        # Time complexity - O(n)

        # Template for dp recursive
        # if in memo, return
        # base case
        # recursive relation = memo[i]
        # return memo[i]
        # def rec(n, memo):
        #     if n in memo:
        #         return memo[n]
        #     if n <= 2:
        #         return n
        #     memo[n] = rec(n-1, memo) + rec(n-2, memo)
        #     return memo[n]
        # return rec(n, {})

        # convert recursion to dp
        # 1. recognize the base cases
        # 2. replace recurrence relation with dp array
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2] = 0, 1, 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]