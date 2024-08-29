class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        longest = 0
        length = 0
        substring = set()
        L = 0

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[L])
                L +=1
                length -= 1
            substring.add(s[i])
            length += 1
            longest = max(longest, length)
        return longest
    

