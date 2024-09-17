class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for n in nums:
            val = abs(n) - 0
            if val == abs(res):
                res = max(n, res)
            elif val < abs(res):
                res = n
        return res