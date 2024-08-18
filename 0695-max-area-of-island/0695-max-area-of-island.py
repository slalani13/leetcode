class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        Largest = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                size = self.exploreSize(grid, r, c, visited)
                Largest = max(Largest, size)
        return Largest

    def exploreSize(self, grid, r, c, visited):
        rowInbounds = 0 <= r < len(grid)
        colInbounds = 0 <= c < len(grid[0])
        if not rowInbounds or not colInbounds:
            return 0
        if (r,c) in visited:
            return 0
        if grid[r][c] == 0:
            return 0
        visited.add((r,c))
        size = grid[r][c]
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        for dr, dc in directions:
            size += self.exploreSize(grid, r+dr, c+dc, visited)
        return size