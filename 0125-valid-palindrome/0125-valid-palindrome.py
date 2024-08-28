class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ""
        for i in range(len(s)):
            if s[i].isalnum():
                phrase += s[i].lower()
        L,R = 0, len(phrase)-1
        while L <= R:
            if phrase[L] != phrase[R]:
                return False
            L += 1
            R -= 1
        return True