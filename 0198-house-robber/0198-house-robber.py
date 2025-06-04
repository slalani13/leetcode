class Solution:
    def rob(self, nums: List[int]) -> int:
        # subproblem - What is the max if I choose to rob this house? I can choose to rob this house or the next house. I want the max between my choices
        # recursive relation: rob(n) = max(nums[i] + rob(i+2), rob(i+1))
        # topological order - use for loop to iterate through nums
        # base case: if no houses, max is 0, if one house max is nums[i]
        # original question: max amount of profit with n houses
        # time: n subproblems * O(1) = O(n)

        # memo and base case
        # recursive relastion
        # return memo[n]
        n = len(nums)-1
        def rec(n, memo):
            if n == -1:
                return 0
            if n == 0:
                return nums[n]
            if n in memo:
                return memo[n]
            memo[n] = max(nums[n] + rec(n-2, memo), rec(n-1, memo))
            return memo[n]
        return rec(n, {})

        # rec(3, {1: 1, 2: 4}), memo[3] = max(1 + 1, rec(2, memo)))
        # rec(1, {}), memo[1] = max(1+ 0, 1)))
        # rec(-1, {}) -> 0
        # rec(0, {}) -> nums[0]
        # rec(2, {1:1, }), memo[2] = max(3+1, 1)
