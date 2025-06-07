class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # start at index 1 and count 1
        # if nums[i] == nums[i-1], increase count by 1. If count <= 2, then set nums[j] = nums[i]
        # because the occurrence of this number is allowed
        # if number changes, this is a new number count is reset to 1, update j value and increment j
        # if count > 2: increase i
        # [1,1, 2, 2, 3, 3], count=1
        #    i  
        #.   j     

        j = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j