class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set()
        for n in nums:
            s.add(n)
        for n in nums:
            if n-1 in s:
                continue
            else:
                cur = 1
                while n+1 in s:
                    cur += 1
                    n += 1
                longest = max(longest, cur)
        return longest