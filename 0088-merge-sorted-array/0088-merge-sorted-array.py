class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = 0, 0
        new_arr = []
        while ptr1 < m and ptr2 < n:
            if nums1[ptr1] <= nums2[ptr2]:
                new_arr.append(nums1[ptr1])
                ptr1+=1
            else:
                new_arr.append(nums2[ptr2])
                ptr2+=1
        while ptr2 < n:
            new_arr.append(nums2[ptr2])
            ptr2+=1
        while ptr1 < m:
            new_arr.append(nums1[ptr1])
            ptr1+=1
        
        for i in range(len(new_arr)):
            nums1[i] = new_arr[i]

        