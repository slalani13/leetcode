class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for n in nums:
            hashmap[n] += 1
        
        maxVal = 0
        ans = -1
        for key, val in hashmap.items():
            if val > maxVal:
                maxVal = val
                ans = key
        return ans