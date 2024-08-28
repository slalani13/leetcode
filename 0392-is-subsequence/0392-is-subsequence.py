class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # iterate through S and keep a pointer at t.
        if len(s) == 0:
            return True
        ptr = 0
        for i in range(len(s)):
            value = s[i]
            while ptr < len(t) and t[ptr] != value:
                ptr+=1
                continue
            if ptr >= len(t):
                return False
            ptr += 1
        return True
                
