class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # SRTBOT
        # Subproblem: How much does it cost to reach the i-1 and i-2 step? As getting the min will provide the min-cost before reaching i
        # Recursive relation: F(i) = min(F(i-1), F(i-2))
        # Topology: linear, for loop from 0 to i
        # Base case: steps 0 cost is cost[0] and step 1 cost is cost[1]
        # Original problem: F(n)
        # Time: O(n)
        # def rec(n, memo):
        #     if n == 0:
        #         return cost[0]
        #     if n == 1:
        #         return cost[1]
        #     if n in memo:
        #         return memo[n]
        #     memo[n] = cost[n] + min(rec(n-1, memo), rec(n-2, memo))
        #     return memo[n]
        # return rec(n, defaultdict(int))
        # [10, 15, 30, 0], n=3, memo = {1: 15, 2: 30, 0: 10, 3: 15}
        # rec(3) = cost[3] + min(30, 15) = 15
        # rec(2) = 20 + min(15, 10) -> 30
        # rec(1) -> 15
        # rec(0) -> 10

        # convert to dp, use base cases to start dp array of size n
        if len(cost) <= 2:
            return cost[len(cost)-1]
        n = len(cost)
        cost.append(0)
        dp = [0] * (n+1)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n+1):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return dp[n]


