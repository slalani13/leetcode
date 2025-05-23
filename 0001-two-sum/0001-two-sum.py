class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} # num : idx
        for idx, num in enumerate(nums):
            key = target - num
            if key in hashmap and hashmap[key] != idx:
                return  [hashmap[key], idx]
            hashmap[num] = idx
        