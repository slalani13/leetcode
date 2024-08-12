class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # represent 26 letters in the alphabet
        lettersS = [0]*26
        lettersT = [0]*26
        for l in s:
            index = ord(l) - ord('a')
            lettersS[index] += 1
        for l in t:
            index = ord(l) - ord('a')
            lettersT[index] += 1
        if lettersS == lettersT:
            return True
        return False
        