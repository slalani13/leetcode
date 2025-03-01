class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ddict = {}
        for i,n in enumerate(nums):
            val = target - n
            if val in ddict:
                return [i, ddict[val]]
            else:
                ddict[n] = i