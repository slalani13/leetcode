class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res, comb = [], []
        def backtrack(x, idx):
            if x == 0:
                res.append(comb[:])
                return
            if x < 0:
                return
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                backtrack(x-candidates[i], i)
                comb.pop()
        backtrack(target, 0)
        return res