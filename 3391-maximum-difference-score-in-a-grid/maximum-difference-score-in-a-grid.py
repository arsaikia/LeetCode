class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        @cache
        def dfs(row, col):
            
            if row not in range(ROWS) or col not in range(COLS):
                return float("-inf")
            
            return max(grid[row][col], dfs(row + 1, col), dfs(row, col + 1))
                
        
        res = float("-inf")
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, -grid[i][j] + dfs(i + 1, j), -grid[i][j] + dfs(i, j + 1))
        return res
            
        