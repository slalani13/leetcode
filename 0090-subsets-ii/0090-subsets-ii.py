class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        nums.sort()

        def backtrack(i):
            if i == len(nums):
                res.append(subset[:])
                return
            # choose to include i
            subset.append(nums[i])
            backtrack(i+1)
            # choose to never include i
            subset.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            backtrack(i+1)

        backtrack(0)
        return res