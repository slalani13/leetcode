class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in map1:
                return [i,map1[key]]
            else:
                map1[nums[i]] = i
