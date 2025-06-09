class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use negative marking, mark each value as the negative of itself first
        # [1, -3, 4, 2, 2]
        # idx = 3, nums[1] = -3
        for num in nums:
            idx = abs(num)
            if nums[idx] < 0:
                return idx
            nums[idx] = -nums[idx]
        
