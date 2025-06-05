class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # two cases, max subarray is in the middle or it loops across
        # if we have a max_subarray, then we will have a min_subarray be the rest of the array
        # as we iterate, we want to obtain the current_sum = max between the array sum or the ucrrent integer as we can start the array in the middle
        # 
        min_sum = nums[0]
        max_sum = nums[0]
        cur_max, cur_min = 0, 0
        total_sum = 0
        for R in range(len(nums)):
            cur_max = max(cur_max + nums[R], nums[R])
            max_sum = max(cur_max, max_sum)
            cur_min = min(cur_min + nums[R], nums[R])
            min_sum = min(cur_min , min_sum)
            total_sum += nums[R]
        if max_sum < 0:
            return max_sum
        else:
            return max(total_sum-min_sum, max_sum)
        
        