class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
        UP_WALL = 0
        DOWN_WALL = ROWS
        RIGHT_WALL = COLS
        LEFT_WALL = -1
        i, j = 0,0

        direction = RIGHT

        while len(res) != ROWS * COLS:
            if direction == RIGHT:
                while j < RIGHT_WALL:
                    res.append(matrix[i][j])
                    j += 1
                i, j = i+1, j-1
                RIGHT_WALL -= 1
                direction = DOWN
            elif direction == DOWN:
                while i < DOWN_WALL:
                    res.append(matrix[i][j])
                    i += 1
                i, j = i-1, j -1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while j > LEFT_WALL:
                    res.append(matrix[i][j])
                    j -= 1
                i, j = i-1, j+1
                LEFT_WALL += 1
                direction = UP
            else:
                while i > UP_WALL:
                    res.append(matrix[i][j])
                    i -= 1
                i, j = i+1, j+1
                UP_WALL += 1
                direction = RIGHT
        return res
                    