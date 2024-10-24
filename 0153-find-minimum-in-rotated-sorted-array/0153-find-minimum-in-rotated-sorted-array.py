class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        L, R = 0, len(nums) - 1

        while L < R:
            mid = L + (R-L) // 2
            if nums[mid] < nums[R]:
                R = mid
            else:
                L = mid + 1
        
        return nums[L]