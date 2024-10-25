class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        s1_state = [0] * 26
        s2_state = [0] * 26
        for s in s1:
            s1_state[ord(s) - ord('a')] += 1
        
        n = len(s1)
        L, R = 0, 0
        
        while R <= len(s2):
            while R-L < n:
                s2_state[ord(s2[R]) - ord('a')] += 1
                R += 1
            if s1_state == s2_state:
                return True
            if R < len(s2):
                s2_state[ord(s2[R]) - ord('a')] += 1
            s2_state[ord(s2[L]) - ord('a')] -= 1
            L+= 1
            R+= 1
        return False
        