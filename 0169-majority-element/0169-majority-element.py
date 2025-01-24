class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # candidate, count = nums[0], 0

        # for i in range(len(nums)):
        #     if count == 0:
        #         candidate = nums[i]
        #         count += 1
        #     elif nums[i] == candidate:
        #         count += 1
        #     else:
        #         count -= 1
        # return candidate
        def rec(i, candidate, count):
            if i == len(nums):
                return candidate
            # check if nums[i] == candidate
            if count == 0:
                return rec(i+1, nums[i], count+1)
            elif nums[i] == candidate:
                return rec(i+1, candidate, count+1)
            # if not
            else:
                return rec(i+1, candidate, count-1)
        return rec(0, nums[0], 0)
