class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        # l, r = 0,0
        # while r < n:
        #     if nums[r] != val:
        #         nums[l] = nums[r]
        #         l += 1
        #     r += 1
        # return l

        def rec(index, left):
            if (index == len(nums)):
                return left
            # nums[i] != val
            if nums[index] != val:
                nums[left] = nums[index]
                return rec(index+1, left+1)

            # nums[i] == val
            return rec(index+1, left)
        return rec(0,0)