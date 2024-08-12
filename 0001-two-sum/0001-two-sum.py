class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i, n in enumerate(nums):
            key, value = n, i
            hashMap[key] = value
        for i, n in enumerate(nums):
            goal = target - n
            if goal in hashMap and hashMap[goal] != i:
                return i, hashMap[goal]
        