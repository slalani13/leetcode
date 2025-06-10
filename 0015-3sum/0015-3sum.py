class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 3 pointers a, b, c 
        # sort the array and shift a and b when they equal the previous value
        # [-4, -1, -1, 0, 1, 2] res = []
        #              a  bc 
        # use 2 pointers to iterate through array
        nums.sort()
        res = []
        for a in range(len(nums)):
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b = a+1
            c = len(nums)-1
            while b < c:
                ssum = nums[a] + nums[b] + nums[c]
                if ssum == 0:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b-1]:
                        b += 1
                elif ssum < 0:
                    b += 1
                else:
                    c -= 1
        return res
            
