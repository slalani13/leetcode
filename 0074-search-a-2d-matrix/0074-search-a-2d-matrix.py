class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # given a sorted matrix and a target, return true if target is in matrix
        # since we know the search range and it is ordered, we can use binary search
        # run binary search to find row, then run again to find target within the row
        # print("I am here")
        # return False
        # first binary search
        target_row = -1
        left, right = 0, len(matrix)-1
        # print("I am here")
        while left <= right:
            mid = left + (right-left) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                target_row = mid
                break
            elif matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
        # print('here')
        if target_row == -1:
            return False
        
        # second binary search
        left, right = 0, len(matrix[target_row])
        while left <= right:
            mid = left + (right-left) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False