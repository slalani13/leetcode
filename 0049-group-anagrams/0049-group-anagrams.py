class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        # map key: tuple, val: list of strings
        m = dict()
        for s in strs:
            l = [0]*26
            for c in s:
                index = ord(c) - ord('a')
                l[index] += 1
            key = tuple(l)
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]
        return m.values()
