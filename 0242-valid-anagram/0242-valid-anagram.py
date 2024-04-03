class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for l in s:
            if l in s_map:
                s_map[l] += 1
            else:
                s_map[l] = 1
        for l in t:
            if l in t_map:
                t_map[l] += 1
            else:
                t_map[l] = 1
        if s_map == t_map:
            return True
        return False
        