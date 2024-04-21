class Solution:
    def isPalindrome(self, s: str) -> bool:
        sList = [val.lower() for val in s if val.isalnum()]
        string1 = "".join(sList)
        print(string1)
        reverseString = ""
        for i in range(len(string1)-1, -1, -1):
            reverseString += string1[i]
        print(reverseString)
        if string1 == reverseString:
            return True
        return False
