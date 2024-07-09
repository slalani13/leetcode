class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0]*3
        for i in range(len(nums)):
            counts[nums[i]] += 1
        k=0
        for i in range(len(counts)):
            for j in range(counts[i]):
                nums[k] = i
                k+=1
        