class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # abc, pqr, l, r = 0, 0
        # iterate through smaller string, then iterate through remainder of other string
        res = ""
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            res += word1[i]
            res += word2[i]
        if len(word1) > len(word2):
            for i in range(min_length, len(word1)):
                res += word1[i]
        elif len(word2) > len(word1):
            for i in range(min_length, len(word2)):
                res += word2[i]
        return res
