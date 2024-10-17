class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, subset = set(), []

        def backtrack(i):
            if i == len(nums):
                s = sorted(subset)
                s = tuple(s)
                res.add(s)
                return
            # choose to add i 
            subset.append(nums[i])
            backtrack(i+1)
            # choose to not add i
            subset.pop()
            backtrack(i+1)

        backtrack(0)
        result = list(res)
        return result