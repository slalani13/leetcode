class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in nums:
            # print(n)
            if n-1 not in numSet:
                #start of a sequence
                length = 1
                while (n+1) in numSet:
                    length += 1
                    n += 1
                    # print(n)
                longest = max(length, longest)
        return longest
