class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ddict = {}
        for i,n in enumerate(nums):
            ddict[n] = i
        for i,n in enumerate(nums):
            value = target - n
            if value in ddict and ddict[value] != i:
                return [i, ddict[value]]