class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        
        def backtrack(i):
            #base case
            if i >= len(nums):
                res.append(sol[:])
                return
            # make a decision
            backtrack(i+1)

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        backtrack(0)
        return res