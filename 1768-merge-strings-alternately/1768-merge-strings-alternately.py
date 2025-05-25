class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # abc, pqr, l, r = 0, 0
        # iterate through smaller string, then iterate through remainder of other string
        res = []
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:])
        res.append(word2[i:])
        return "".join(res)
