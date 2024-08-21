class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countM = [0]*26
        countR = [0]*26
        for c in magazine:
            index = ord(c) - ord('a')
            countM[index] += 1
        for c in ransomNote:
            index = ord(c) - ord('a')
            countR[index] += 1
        for i in range(26):
            if countR[i] > countM[i]:
                return False
        return True