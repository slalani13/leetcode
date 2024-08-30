class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations, comb = [], []

        def dfs(i):
            if len(comb) == k:
                combinations.append(comb.copy())
                return
            if i > n:
                return

            for j in range(i, n+1):
                comb.append(j)
                dfs(j+1)
                comb.pop()

        dfs(1)
        return combinations