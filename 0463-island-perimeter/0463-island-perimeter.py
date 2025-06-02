class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # use dfs when grid[i][j] == 1
        # dfs calls on each neighbor
        # if nei is water, per + 1

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        perimeter = [0]

        def dfs(i, j):
            # check if inbounds or water, p += 1
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0 :
                perimeter[0] += 1
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                dfs(i+dr, j+dc)
            
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter[0]
        return perimeter[0]