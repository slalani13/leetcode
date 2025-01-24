class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # consider a sorted array in non-decreasing order
        # remove the duplicates in place such that each unique element appears only once
        # return the number of unique elements, k

        # Cases:
        # length of array is always at least 1
        # [1, 1, 2] -> [1, 2, _]
        # Base case: [1], [] -> if len(nums) <= 1: return len(nums)
        # [1, 1, 1, 1, 1] -> [1, _]: k=1
        # [1, 2]
        if len(nums) <= 1:
            return len(nums)

        L, R = 1, 1
        while R < len(nums):
            # what is the condition at which we stop iterating and process?
            # when nums[R] does not equal its previous value, i.e new unique val
            if nums[R] != nums[R-1]:
                nums[L] = nums[R]
                L += 1
            R += 1
        return L
        

