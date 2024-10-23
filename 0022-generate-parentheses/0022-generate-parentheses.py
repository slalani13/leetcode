class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        
        def backtrack(s, open, close):
            if len(s) == 2*n:
                res.append(s)
            
            if open < n:
                backtrack(s + "(", open+1, close)
            if close < open:
                backtrack(s+")", open, close+1)
        
            return res
        return backtrack("", 0, 0)
        