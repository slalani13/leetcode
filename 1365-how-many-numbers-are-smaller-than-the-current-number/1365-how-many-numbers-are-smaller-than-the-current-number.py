class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        hashmap = {}
        output = []
        for i, n in enumerate(temp):
            if n not in hashmap:
                hashmap[n] = i
        
        for n in nums:
            output.append(hashmap[n])
        return output
            