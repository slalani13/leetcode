class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # use prefix sum and suffix sums, subtract prefix - suffix and get 0. If not 0, return -1
        prefixArr = [0] * len(nums)
        suffixArr = [0] * len(nums)
        prefix = 0
        suffix = 0
        suffixIdx = len(nums)-1
        for i in range(len(nums)):
            prefix += nums[i]
            prefixArr[i] = prefix
            suffix += nums[suffixIdx]
            suffixArr[suffixIdx] = suffix
            suffixIdx -= 1
        # print(prefixArr, suffixArr)
        for i in range(len(nums)):
            if prefixArr[i] - suffixArr[i] == 0:
                return i
        return -1