class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        for i, num in enumerate(nums):
            if i == 0 and num > nums[i+1]:
                return i
            elif 0 < i < len(nums)-1 and nums[i-1] < num > nums[i+1]:
                return i
            elif i == len(nums)-1 and num > nums[i-1]:
                return i
