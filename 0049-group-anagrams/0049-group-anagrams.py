class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        groups = {} # tuple to list of words

        for i in range(len(strs)):
            s = [0] * 26
            for l in strs[i]:
                idx = ord(l) - ord('a')
                s[idx] += 1
            if tuple(s) in groups:
                groups[tuple(s)].append(strs[i])
            else:
                groups[tuple(s)] = [strs[i]]
        for val in groups.values():
            res.append(val)
        return res
            