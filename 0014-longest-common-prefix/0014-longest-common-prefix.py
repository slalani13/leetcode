class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLength = float("inf")
        for s in strs:
            minLength = min(minLength, len(s))
        i=0
        while i < minLength:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i+=1
        return strs[0][:i]
        