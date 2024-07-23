class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if i >= len(candidates) or total > target:
                return
            # choose to add candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
        dfs(0, cur, 0)
        return res