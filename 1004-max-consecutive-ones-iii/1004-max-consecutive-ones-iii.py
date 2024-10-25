class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxW = 0
        numZeros = 0

        L = 0

        for R in range(len(nums)):
            if nums[R] == 0:
                numZeros += 1
            
            while numZeros > k:
                if nums[L] == 0:
                    numZeros -= 1
                L += 1
            
            w = R-L+1
            maxW = max(maxW, w)
        return maxW