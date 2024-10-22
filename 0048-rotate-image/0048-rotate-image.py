class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # to rotate matrix 90 degrees, transpose and then reverse each row

        #transpose matrix i.e [i,j] = [j,i] around the diagonal
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # reverse each row
        for i in range(n):
            matrix[i].reverse()
        
        return matrix