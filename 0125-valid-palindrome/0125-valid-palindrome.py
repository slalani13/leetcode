class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in range(len(s)):
            if s[i].isalnum():
                newS += s[i].lower()
        beg,end = 0, len(newS)-1
        while beg <= end:
            if newS[beg] != newS[end]:
                return False
            beg += 1
            end -= 1
        return True