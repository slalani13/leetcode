class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix)-1

        while L <= R:
            mid = L + (R-L) // 2
            if target in matrix[mid]:
                return True
            elif target < matrix[mid][0]:
                R = mid - 1
            else:
                L = mid + 1
        return False