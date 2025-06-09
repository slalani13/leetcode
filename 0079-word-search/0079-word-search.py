class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c, char_idx, visited):
            # base case if out of bounds or does not equal letter
            if not (0 <= r < ROWS and 0 <= c < COLS) or board[r][c] != word[char_idx] or (r, c) in visited:
                return False
            if char_idx == len(word)-1:
                return True
            # visited((0, 0), (0, 1), )
            visited.add((r, c))
            up = dfs(r-1, c, char_idx+1, visited) # false
            down = dfs(r+1, c, char_idx+1, visited) # false
            right = dfs(r, c+1, char_idx+1, visited) # calls dfs(0, 2, 2, visited)
            left = dfs(r, c-1, char_idx+1, visited)
            if up or down or left or right:
                return True
            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0, set()):
                    return True
        return False

