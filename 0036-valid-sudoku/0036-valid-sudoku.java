class Solution {
    public boolean isValidSudoku(char[][] board) {
        // use sets for row and column
        Map<Integer, Set<Character>> rowMap = new HashMap<>();
        Map<Integer, Set<Character>> colMap = new HashMap<>();
        Map<String, Set<Character>> gridMap = new HashMap<>();
        // use map for grid key: (r // 3, c // 3) -> set(1-9)
        for (int i=0; i < board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                if (board[i][j] == '.') {
                    continue;
                }
                String gridKey = (i / 3) + "-" + (j / 3);

                rowMap.putIfAbsent(i, new HashSet<Character>());
                colMap.putIfAbsent(j, new HashSet<Character>());
                gridMap.putIfAbsent(gridKey, new HashSet<Character>());

                
                if (rowMap.get(i).contains(board[i][j]) || colMap.get(j).contains(board[i][j]) || gridMap.get(gridKey).contains(board[i][j])) {
                    return false;
                }

                rowMap.get(i).add(board[i][j]);
                colMap.get(j).add(board[i][j]);
                gridMap.get(gridKey).add(board[i][j]);
            }
        }
        return true;
    }
}