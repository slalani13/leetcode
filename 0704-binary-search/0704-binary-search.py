class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #edge cases
        if len(nums) == 0:
            return -1
        L = 0
        R = len(nums)-1
        mid = (L+R)//2
        print(mid)
        while L <= R:
            if target < nums[mid]:
                R=mid-1
                mid = (L+R)//2
            elif target > nums[mid]:
                L=mid+1
                mid = (L+R)//2
            else:
                return mid
        return -1