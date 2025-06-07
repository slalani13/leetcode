class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # nums and target both positive, return the minimal length of a subarray greater than or equal to taret
        L= 0
        curSum = 0
        minWindow = float("inf")
        for R in range(len(nums)):
            curSum += nums[R]
            while curSum >= target:
                minWindow = min(R-L+1, minWindow)
                curSum -= nums[L]
                L += 1

        return minWindow if minWindow != float("inf") else 0
            
        # [2, 3, 1, 2, 4, 3] L=3,R=5, curSum=6, t=7, min=3
            