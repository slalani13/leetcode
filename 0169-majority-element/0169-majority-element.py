class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = nums[0], 0

        for i in range(len(nums)):
            if count == 0:
                candidate = nums[i]
                count += 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1
        return candidate