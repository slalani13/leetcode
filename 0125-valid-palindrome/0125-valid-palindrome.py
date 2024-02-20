class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        s = s.lower()
        for c in s:
            if c.isalnum():
                res += c
            else:
                continue
        print(res)
        i=0
        j=len(res)-1

        while i < j:
            if res[i] != res[j]:
                return False
            i+=1
            j-=1
        return True
