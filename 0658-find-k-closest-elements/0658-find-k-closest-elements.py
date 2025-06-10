class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # use lower bound binary search to find index <= x
        # if index is left of array, return index:index+k
        # if index is right of array, return index-k:index
        # else, check left and right, if k-left <= right-k: move left pointer, else move right
        # [1, 2, 3, 4, 5] k=4, x=3
        #  F  F  T  T  T
        # [1, 4, 8, 12] x=3
        #  F  T  T  T
        def binarySearch():
            l, r = 0, len(arr)-1
            while l < r:
                mid = l+(r-l) // 2
                if arr[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            return l
        
        right = binarySearch()
        left = right-1
        while right-left-1 < k:
            if left < 0:
                return arr[:k]
            elif right >= len(arr):
                return arr[-k:]
            else:
                if (x-arr[left]) <= arr[right]-x:
                    left -= 1
                else:
                    right += 1
        return arr[left+1: right]