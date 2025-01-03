class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s) + 1
        dp = [False] * n
        dp[0] = True
        trues = [0]

        for i in range(n):
            for j in trues:
                if s[j:i] in wordDict:
                    dp[i] = True
                    trues.append(i)
                    break
        
        return dp[-1]