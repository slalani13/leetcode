class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        prefix = ""
        for s in strs:
            min_length = min(min_length, len(s))
        for i in range(min_length):
            for word in strs:
                if word[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

            