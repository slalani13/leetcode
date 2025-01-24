class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # if len(nums) <= 1:
        #     return len(nums)

        # L, R = 1, 1
        # while R < len(nums):
        #     if nums[R] != nums[R-1]:
        #         nums[L] = nums[R]
        #         L += 1
        #     R += 1
        # return L

        # write this recursively
        # [ 1, 2, 3], [1, 1, 1]
        def rec(index, unique_index):
            if index == len(nums):
                return unique_index
            
            # case when index != index-1
            if index == 0 or nums[index] != nums[index-1]:
                nums[unique_index] == nums[index]
                return rec(index+1, unique_index+1)

            # case when index == index-1
            return (index+1, unique_index)
        

