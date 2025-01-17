class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        # for i in range(len(nums)):
        #     if nums[i] in s:
        #         return True
        #     s.add(i)
        
        # return False
        
        def rec(i, s):
            if i==len(nums):
                return False
            if (nums[i] in s):
                return True
            s.add(nums[i])
            # print("running state ",i,s)
            return rec(i+1, s)
            

        return rec(0, set())
