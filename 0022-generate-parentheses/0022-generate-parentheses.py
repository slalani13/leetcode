class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(left, right, comb):
            if len(comb) == 2*n:
                res.append(comb)
                return
            if left > right:
                backtrack(left, right+1, comb + ")")
            if left < n:
                backtrack(left+1, right, comb+ "(")

        backtrack(0, 0, "")
        return res