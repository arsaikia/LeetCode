class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        cache = obstacleGrid[::]
        for r in range(ROWS):
            for c in range(COLS):
                if cache[r][c] == 1:
                    cache[r][c] = -1

        def traverse(grid, row, col, ROWS, COLS, ways):
            # Nagative base case
            if row == ROWS or col == COLS or grid[row][col] == -1:
                return 0
            
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            if ways[row][col] > 0:
                return ways[row][col]
            
            ways[row][col] = (
                traverse(grid, row + 1, col, ROWS, COLS, ways) + 
                traverse(grid, row, col + 1, ROWS, COLS, ways))
            
            return ways[row][col]

        return traverse(obstacleGrid, 0, 0, ROWS, COLS, cache)

        