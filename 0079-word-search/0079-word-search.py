class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0] or (i,j) in visited:
                return False
            visited.add((i,j))
            if (dfs(i+1,j, word[1:]) or dfs(i-1, j, word[1:]) or dfs(i, j+1, word[1:]) or dfs(i, j-1, word[1:])):
                return True
            visited.remove((i,j))
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, word):
                    return True
        return False
        