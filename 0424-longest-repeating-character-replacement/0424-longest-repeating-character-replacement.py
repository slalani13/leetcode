class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # return longest substring with at most K replacements
        longest = 0
        counter = defaultdict(int) # key= letter, value= freq
        l = 0
        maxfreq = 0

        for r in range(len(s)):
            counter[s[r]] += 1
            maxfreq = max(maxfreq, counter[s[r]])
            while r-l+1 - maxfreq > k:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
        # s="ABAB", map={A:2, B:1, }, maxF = 1, w=1, R=1, L=0
            
