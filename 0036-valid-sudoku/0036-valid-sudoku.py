class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        squareMap = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue
                r = row//3
                c = col//3
                if board[row][col] in rowMap[row]:
                    return False
                if board[row][col] in colMap[col]:
                    return False
                if board[row][col] in squareMap[(r,c)]:
                    return False
                rowMap[row].add(board[row][col])
                colMap[col].add(board[row][col])
                squareMap[(r,c)].add(board[row][col])
        return True