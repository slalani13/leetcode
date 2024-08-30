class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations, comb = [], []

        def dfs(i):
            if len(comb) == k:
                combinations.append(comb.copy())
                return
            if i > n:
                return
            comb.append(i)
            dfs(i+1)
            comb.pop()
            dfs(i+1)
        dfs(1)
        return combinations