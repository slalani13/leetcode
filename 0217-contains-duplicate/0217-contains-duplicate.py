class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        myset = set()
        for i in range(len(nums)):
            if nums[i] not in myset:
                myset.add(nums[i])
                # print(myset)
            else:
                return True
        return False
        