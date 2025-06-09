class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # sort an array, let's do merge sort
        # split into 2, once returned merge it
        # base case arr of size 1 is returned
        def merge(nums, s, m, e):
            left = nums[s:m+1]
            right = nums[m+1:e+1]
            i, j, k = s, 0, 0 # this is the pointers for nums, left, and right
            
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            # one of the arrays could be longer, need to finish iterating
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(nums, s, e):
            if s == e:
                return nums
            m = (s + e) // 2
            mergeSort(nums, s, m)
            mergeSort(nums, m+1, e)
            merge(nums, s, m, e)
            return nums
        return mergeSort(nums, 0, len(nums)-1)
        
        

            