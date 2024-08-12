class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''
        for c in s:
            if c.isalnum():
                newS += c.lower()
        start, end = 0, len(newS)-1
        while start <= end:
            if newS[start] != newS[end]:
                return False
            start+= 1
            end -= 1
        return True