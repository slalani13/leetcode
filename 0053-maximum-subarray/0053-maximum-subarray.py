class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # using nums subarray return largest sum of a subarray
        # use Kadane's algorithm, right pointer always moves, left pointer shifts when negative sum
        max_sum = nums[0]
        current_sum = 0
        L = 0

        for R in range(len(nums)):
            if current_sum < 0:
                current_sum = 0
                L = R
            current_sum += nums[R]
            max_sum = max(current_sum, max_sum)

        return max_sum
        # [-1, -5, -4] works