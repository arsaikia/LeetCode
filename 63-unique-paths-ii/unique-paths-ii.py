class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0 for col in range(len(obstacleGrid[0]))] for row in range(len(obstacleGrid))]

        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = - 1
                
        def getPath(row, col):
            if row not in range(ROWS) or col not in range(COLS) or obstacleGrid[row][col] == -1:
                return 0

            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            if paths[row][col]:
                return paths[row][col]
            
            down, right = getPath(row + 1, col), getPath(row, col + 1)

            paths[row][col] = down + right
            return paths[row][col]
        
        return getPath(0, 0)
            


        