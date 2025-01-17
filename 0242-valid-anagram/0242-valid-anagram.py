class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1 = [0] * 26
        t1 = [0] * 26

        for i in range(len(s)):
            s_idx = ord(s[i]) - ord('a')
            t_idx = ord(t[i]) - ord('a')
            s1[s_idx] += 1
            t1[t_idx] += 1
        
        if s1 != t1:
            return False
        return True
        
        # def rec(i, s1, t1):
        #     if len(s) != len(t):
        #         return False
        #     if i == len(s):
        #         if s1 != t1:
        #             return False
        #         else:
        #             return True
                
        #     s_idx = ord(s[i]) - ord('a')
        #     t_idx = ord(t[i]) - ord('a')
        #     s1[s_idx] += 1
        #     t1[t_idx] += 1
        #     return rec(i+1, s1, t1)
        
        # return rec(0, [0]*26, [0]*26)