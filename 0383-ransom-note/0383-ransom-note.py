class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = [0]*26
        for c in magazine:
            index = ord(c) - ord('a')
            mag[index] +=1
        for c in ransomNote:
            if mag[ord(c) - ord('a')] == 0:
                return False
            else:
                mag[ord(c) - ord('a')] -= 1
        return True