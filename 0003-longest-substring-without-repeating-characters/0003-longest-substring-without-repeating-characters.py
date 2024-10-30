class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        longest = 0
        sett = set()

        for r in range(n):
            #while window is not valid
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = (r-l) + 1
            longest = max(w, longest)
            sett.add(s[r])
        
        return longest