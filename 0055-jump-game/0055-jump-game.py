class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [2, 3, 1, 1, 4] 
        n = len(nums)
        destination = n-1
        for i in range(n-2, -1, -1):
            if i+nums[i] >= destination:
                destination = i
        return destination == 0