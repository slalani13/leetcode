class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        L, R = 0, n-1

        while L < R:
            mid = L + (R-L+1) // 2
            if nums[mid] > nums[mid+1]:
                R = mid
            else:
                L = mid + 1
        return R