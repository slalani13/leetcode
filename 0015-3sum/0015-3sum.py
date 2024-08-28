class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numSort = sorted(nums)
        s = set()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            if i != 0 and numSort[i] == numSort[i-1]:
                continue
            while j < k:
                if numSort[i] + numSort[j] + numSort[k] == 0:
                    s.add(tuple([numSort[i], numSort[j], numSort[k]]))
                    j += 1
                    continue
                elif numSort[i] + numSort[j] + numSort[k] < 0:
                    j += 1
                else:
                    k -= 1
        return s
