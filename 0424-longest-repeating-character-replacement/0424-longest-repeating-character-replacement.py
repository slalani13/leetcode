class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # check if window is valid - we have substring with one character only using k replacements
        # if window is valid, we can increase the window
        # s = "ABAB" k = 2
        # counts = {A: 1} , r=, l=0
        longest = 0 # 1
        l= 0
        counts = [0] * 26
        for r in range(len(s)):
            # adding right char
            idx = ord(s[r]) - ord('A')
            counts[idx] += 1
            # if window is invalid, remove left char
            if (r-l+1)-max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            else:
                longest = max(longest, r-l+1)

        return longest