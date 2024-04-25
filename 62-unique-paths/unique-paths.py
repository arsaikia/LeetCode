class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        memo = {}

        def findPaths(row, col):
            nonlocal ROWS, COLS

            if (row, col) in memo:
                return memo[(row, col)]

            if row not in range(ROWS) or col not in range(COLS):
                return 0
            
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            down = findPaths(row + 1, col)
            right = findPaths(row, col + 1)
            
            memo[(row, col)] = right + down

            return memo[(row, col)]
        
        return findPaths(0, 0)
        