class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # return all possible subsets - O(2^n) because there are 2^n results
        # [] -> choose to add i, choose to not add i
        # base cases: if i == length(add to res)
        res, subset = [], []
        def backtrack(i):
            if i == len(nums):
                res.append(subset[:])
                return
            # don't choose i and backtrack(i+1)
            backtrack(i+1)
            # choose i
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()

        backtrack(0)
        return res
        