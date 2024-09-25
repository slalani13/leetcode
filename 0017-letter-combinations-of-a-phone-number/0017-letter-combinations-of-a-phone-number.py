class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dmap = {"2":"abc", "3": "def", "4": "ghi", "5":"jkl", "6": "mno", "7": "pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def backtrack(comb, next_digits):
            if len(next_digits) == 0:
                res.append(comb)
                return
            for letter in dmap[next_digits[0]]:
                backtrack(comb + letter, next_digits[1:])
        backtrack("", digits)
        return res
            