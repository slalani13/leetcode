class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [float('inf')] * (n)

        def dp(n):
            if n <= 1:
                return cost[n]
            if memo[n] != float('inf'):
                return memo[n]
            
            memo[n] = min(dp(n-1), dp(n-2)) + cost[n]
            return memo[n]
        
        return min(dp(n-1), dp(n-2))