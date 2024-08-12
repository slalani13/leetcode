class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(1)
                continue
            res.append(nums[i-1] * res[i-1])
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums) -1:
                curr = nums[i]
                continue
            res[i] *= curr
            curr *= nums[i] 
        return res

