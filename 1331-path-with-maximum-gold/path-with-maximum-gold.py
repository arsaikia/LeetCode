class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def findGoldInPath(row, col, visited):
            if row not in range(ROWS) or col not in range(COLS) or (row, col) in visited or grid[row][col] == 0:
                return 0
            
            visited.add( (row, col) )

            left = findGoldInPath(row, col - 1, visited)
            right = findGoldInPath(row, col + 1, visited)
            top = findGoldInPath(row - 1, col, visited)
            bottom = findGoldInPath(row + 1, col, visited)

            gold = grid[row][col] + max(top, right, bottom, left)
            
            visited.remove( (row, col) )
            return gold
        
        maxGold = 0
        for row in range(ROWS):
            for col in range(COLS):
                maxGold = max(maxGold, findGoldInPath(row, col, visited))
        return maxGold