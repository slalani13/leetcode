class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, n in enumerate(nums):
            hashmap[n] = index
        for idx, n in enumerate(nums):
            val = target - n
            if val in hashmap and hashmap[val] != idx:
                return [hashmap[val], idx]