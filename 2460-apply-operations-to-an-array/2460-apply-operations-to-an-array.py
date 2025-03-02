class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        j=0
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        new_nums = [0]*len(nums)
        for i in range(n):
            if nums[i] != 0:
                new_nums[j] = nums[i]
                j += 1
        return new_nums
        