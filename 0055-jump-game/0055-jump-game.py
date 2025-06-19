class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # return true if you can reach the last index from the first index
        # Subproblems - can we reach the array from index num[i+1:i+num]? If any are true return true, else false
        # recursive relation - F[i] = F[i+1] or F[i+2] or ... F[i+nums[i]]
        # Topology - iterate through the array
        # base case - last index is true
        # Original problem - F(0)
        # Time complexity - O(n)
        n = len(nums)
        # def rec(i, memo):
        #     if i == n-1:
        #         return True
        #     if i in memo:
        #         return memo[i]
        #     for j in range(i+1, i+1+nums[i]):
        #         if j < n:
        #             if rec(j, memo):
        #                 memo[i] = True
        #                 return True
        #     memo[i] = False
        #     return memo[i]
        # return rec(0, {})
        # [2, 3, 1, 1, 4], n = 5, memo = {4: True, 3: True, 2: True, 1: True, 0:True}
        # rec(0), rec(j=1) -> True
        # rec(1), rec(j=2) -> True
        # rec(2), rec(j=3) -> True
        # rec(3), rec(j=4) -> True
        dp = [False] * len(nums)
        dp[-1] = True
        target = n-1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= target:
                dp[i] = True
                target = i
        return dp[0]
            