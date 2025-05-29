class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [100, 4, 200, 1, 3, 2]
        # [ Y.  N   Y.  Y  N. N ]
        s = set(nums)
        longest = 0
        for num in s:
            # is num the start of a sequence
            if num-1 not in s:
                # x = num+1
                length = 1
                n = num
                while n+1 in s:
                    length += 1
                    n += 1
                longest = max(length, longest)
        return longest