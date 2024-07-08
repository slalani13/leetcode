class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = dict()
        for i, num in enumerate(nums):
            m[num] = i
        print(m)
        for i, n in enumerate(nums):
            desired = target - n
            if desired in m and m[desired] != i:
                return m[desired], i
        
