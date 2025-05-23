class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # num : idx
        # [1, 3, 3, 6] 
        for idx, num in enumerate(nums):
            key = target - num
            if key in hashmap:
                return  [hashmap[key], idx]
            hashmap[num] = idx
        