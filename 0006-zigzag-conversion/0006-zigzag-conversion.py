class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        idx, d = 0, 1
        matrix = ["" for _ in range(numRows)]

        for i in range(len(s)):
            matrix[idx] += s[i]
            if idx == 0:
                d = 1
            elif idx == numRows-1:
                d = -1
            idx += d
        
        return "".join(matrix)