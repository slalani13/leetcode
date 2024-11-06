class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = [0] * 26
        longest = 0
        L = 0
        for R in range(n):
            idx = ord(s[R]) - ord('A')
            freq[idx] += 1
            # while window is not valid
            while (R-L+1) - max(freq) > k:
                if L < n-1:
                    idx = ord(s[L]) - ord('A')
                    freq[idx] -= 1
                    L += 1
            w = R-L+1
            longest = max(longest, w)
        return longest