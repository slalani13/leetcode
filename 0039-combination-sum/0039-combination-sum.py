class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # distinct integers candidate array
        # target interger, return all unique combinations of candidates where the chosen numbers sum to target. Can return in any order.
        # the same number can be chosen an unlimited number of times
        # [2, 3, 6, 7] target=7
        # decision tree - choose each element as a path?
        # if sum == target, add to list of solutions
        # each i covers all combinations with nums[i]
        res, sol = [], []
        # intuition: with combinations you can only build from current index left to right
        # to avoid duplicates
        def backtrack(start, ssum):
            if ssum == 0:
                res.append(sol[:])
            elif ssum < 0:
                return
            for i in range(start, len(candidates)):
                # add nums[i] to path
                sol.append(candidates[i])
                backtrack(i, ssum - candidates[i])
                # backtrack from path
                sol.pop()

        backtrack(0, target)
        return res



