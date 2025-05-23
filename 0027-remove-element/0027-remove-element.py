class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # [3, 2, 2, 3] val = 3
        # [2,2,-,-]
        # [2, 2, 3, 3] val = 3
        # sort it, but that changes my order
        # find all vals and move to end
        # iterate reverse and find first non-val element
        # iterate from left and find val and swap, update right pointer again
        # left pointer will keep updating until l == r
        # return k which is the number of elements that aren't val
        n = len(nums)
        r = n-1
        k = 0 # [2233] r = 1, k=2, l = 1
        for l in range(n):
            # updates r to be rightmost non-val element
            while r>=0 and nums[r] == val:
                r-=1
            if nums[l] != val:
                k += 1
            if l < r:
                # if left pointer is val
                if nums[l] == val:
                    nums[l], nums[r] = nums[r], nums[l]
                    k += 1
                    r -= 1
        return k
            