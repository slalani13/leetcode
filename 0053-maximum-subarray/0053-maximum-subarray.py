class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if max(nums) < 0:
            return max(nums)
        largest = float('-inf')
        summ = 0
        for i in range(n):
            summ += nums[i]
            if summ < 0:
                summ = 0
            largest = max(largest, summ)
        return largest