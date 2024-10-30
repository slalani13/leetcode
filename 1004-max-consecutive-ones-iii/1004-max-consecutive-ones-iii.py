class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        maxW = 0
        numZeroes = 0
        for r in range(n):
            if nums[r] == 0:
                numZeroes += 1

            # while window is not valid
            while numZeroes > k:
                if nums[l] == 0:
                    numZeroes -= 1
                l += 1
            
            w = (r-l) + 1
            maxW = max(maxW, w)
        return maxW