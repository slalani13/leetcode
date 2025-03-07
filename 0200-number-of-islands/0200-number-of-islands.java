class Solution {
    public int numIslands(char[][] grid) {
        Set<String> visited = new HashSet<>();
        int count = 0;
        for (int i=0; i<grid.length; i++) {
            for (int j=0; j<grid[0].length; j++) {
                if (dfs(i, j, visited, grid)) {
                    count += 1;
                }
            }
        }
        return count;
    }

    public boolean dfs(int r, int c, Set<String> visited, char[][] grid) {
        if (r < 0 || r >= grid.length ||
         c < 0 || c >= grid[0].length || grid[r][c] == '0' || 
        visited.contains(r + "+" + c)) {
            return false;
        }
        visited.add(r + "+" + c);
        dfs(r+1, c, visited, grid);
        dfs(r-1, c, visited, grid);
        dfs(r, c+1, visited, grid);
        dfs(r, c-1, visited, grid);

        return true;
    }
}