class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = [0] * 26
        for c in s:
            index = ord(c) - ord('a')
            countS[index] += 1
        countT = [0]*26
        for c in t:
            index = ord(c) - ord('a')
            countT[index] += 1
        if countS == countT:
            return True
        return False
        