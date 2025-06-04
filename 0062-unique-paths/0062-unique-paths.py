class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # two inputs m and n, return the number of possible unique paths that a robot cantake to reach the bottom right corner
        # subproblem - How many unique paths can be reached from one position down and one position to the right
        # recursive relation - unique(r,c) = unique(r+1, c) + unique(r, c+1)
        # topological order - iterate through the matrix from m-1, n-1 to 0, 0
        # base case: row m-1 has only one unique path, col n-1 has only one unique path
        # original problem - solve for unique(0, 0)
        # time - O(m*n)
        def rec(r, c, memo):
            if r == m-1 or c == n-1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = rec(r+1, c, memo) + rec(r, c+1, memo)
            return memo[(r, c)]
        return rec(0, 0, {}) 