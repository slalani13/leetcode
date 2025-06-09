class NumMatrix:
    # [0, 5]: 0,0 to 0, 5 goes from row 0 to row 0 and col 0 to col 5
    # [1:0]0, 0 to 1, 0 goes from row 0 to row 1 and column 0 of each row
    # [2:2 ]0, 0 to 2, 2 goes from row 0 to 2 and col 0 to 3 non inclusive 
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.matrixSums = [[0] * (COLS+1) for c in range(ROWS+1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                top = self.matrixSums[r][c+1]
                self.matrixSums[r+1][c+1] = prefix + top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        # example is 1, 1, -> 2, 2
        bottomRight = self.matrixSums[row2][col2]
        top = self.matrixSums[row1-1][col2]
        left = self.matrixSums[row2][col1-1]
        topLeft = self.matrixSums[row1-1][col1-1]
        return bottomRight - top - left + topLeft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)