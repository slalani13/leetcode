class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        s = set()
        for n in nums:
            s.add(n)
        longest = 1
        for n in nums:
            if n-1 in s:
                continue
            else:
                curr = 1
                while n+1 in s:
                    curr += 1
                    n += 1
                longest = max(longest, curr)
        return longest
