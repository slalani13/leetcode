class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge cases
        if len(s) != len(t):
            return False
        ls = [0]*26
        lt = [0]*26
        for c in s:
            index = ord(c) - ord('a')
            ls[index] +=1
        for c in t:
            index = ord(c) - ord('a')
            lt[index] +=1
        if ls == lt:
            return True
        return False
