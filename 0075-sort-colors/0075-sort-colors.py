class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using bucket sort since we know the range is 0-2
        colors = [0] * 3
        for n in nums:
            colors[n] += 1
        j=0
        for i in range(3):
            count = colors[i]
            while count != 0:
                nums[j] = i
                j += 1
                count -= 1
        
        

        