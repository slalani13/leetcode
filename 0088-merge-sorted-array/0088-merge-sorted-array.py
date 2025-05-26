class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # [1, 2, 3, 3, 5, 6] ptr = 3, ptr1 = 2, ptr2 = 0
        # [2, 5, 6]
        #m=3, n=3, m+n
        # iterate from m+n-1 to 0
        # start at nums1[m] and nums2[n] but update nums1[m+n-1]
        ptr = m+n-1
        ptr1 = m-1
        ptr2 = n-1
        while ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[ptr] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ptr] = nums2[ptr2]
                ptr2 -= 1
            ptr -= 1
        # while ptr2 >= 0:
        #     nums1[ptr] = nums2[ptr2]
        #     ptr -= 1
        #     ptr2 -= 1
        
        if ptr2 >=0:
            nums1[:ptr2+1] = nums2[:ptr2+1]


