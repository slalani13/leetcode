class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 2, 3, 4]
        # do prefix[i] = prefix and then update prefix = prefix * nums[i]
        # pre = 24 product = [24, 12, 8, 6]
        # suffix= 24
        # going backwards product[i] = suffix*product[i], suffix *= nums[i] 
        prefix = 1
        suffix = 1
        product = [1] * len(nums)
        for i in range(len(nums)):
            product[i] = prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            product[i] *= suffix
            suffix *= nums[i]
        return product