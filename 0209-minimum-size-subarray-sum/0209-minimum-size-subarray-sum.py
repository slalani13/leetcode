class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, n = 0, len(nums) 
        length = float("inf")
        current_sum = 0
        
        for R in range(n):
            current_sum += nums[R]
            while current_sum >= target:
                length = min(length, R-L+1)
                current_sum -= nums[L]
                L += 1
        
        return length if length != float("inf") else 0