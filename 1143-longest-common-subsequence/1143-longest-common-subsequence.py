class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # two inputs return the length of the lcs, else 0
        # subproblem: LCS = LCS[i:] * LCS[j:] choose 2 substrings and get their project
        # recursive relation: LCS() = max(1+LCS(i+1, j+1), LCS(i, j+1), LCS(i+1, j))
        # this is saying we either include i and j, include i, or include j
        # topology: iterate through both strings until one is none
        # base case: when i == len(text1) or j == len(text2) return 0
        # original problem - LCS(i, j)
        # time - O(m*n) length of both strings 
        memo = {}
        i, j = len(text1)-1, len(text2)-1
        def LCS(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + LCS(i - 1, j - 1)
            else:
                memo[(i, j)] = max(LCS(i, j-1), LCS(i-1, j))
            return memo[(i, j)]
        return LCS(i, j)