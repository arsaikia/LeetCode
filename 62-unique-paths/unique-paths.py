class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        ways = [ [0 for col in range(COLS)] for row in range(ROWS) ]
        ways[-1][-1] = 1

        def traverse(row, col, ROWS, COLS, ways):
            # Nagative base case
            if row == ROWS or col == COLS:
                return 0
            
            if ways[row][col] > 0:
                return ways[row][col]
            
            ways[row][col] = (
                traverse(row + 1, col, ROWS, COLS, ways) + 
                traverse(row, col + 1, ROWS, COLS, ways))
            
            return ways[row][col]

        return traverse(0, 0, ROWS, COLS, ways)

