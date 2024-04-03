class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = dict()
        for i in range(len(nums)):
            val=target - nums[i]
            if val in mydict:
                return i,mydict[val]
            else:
                mydict[nums[i]]=i