class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLUMNS = len(matrix), len(matrix[0]) # 3, 4
        top, bottom = 0, ROWS-1
        while top <= bottom:
            row = bottom + top // 2
            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break
        # check that target exists
        if not (top <= bottom):
            return False
        row = bottom + top // 2    
        L,R = 0, COLUMNS-1
        while L <= R:
            M = R+L // 2
            if target > matrix[row][M]:
                L = M+1
            elif target < matrix[row][M]:
                R = M-1
            else:
                return True
        return False
