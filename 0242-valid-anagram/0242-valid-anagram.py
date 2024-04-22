class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge cases
        if len(s) != len(t):
            return False
        if len(s) == 0:
            return True
        strList = [0]*26
        strList2 = [0]*26
        print(strList)
        for char in s:
            index = ord(char) - ord('a')
            strList[index] += 1
        for char in t:
            index = ord(char) - ord('a')
            strList2[index] += 1
        if strList == strList2:
            return True
        return False