class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in visited:
                    continue
                if grid[row][col] == 1:
                    return self.traverseIslandAndCalculatePerimeter(row, col, ROWS, COLS, visited, grid)
        return 0
                
        
    def traverseIslandAndCalculatePerimeter(self, row, col, ROWS, COLS, visited, grid):
        if row not in range(ROWS) or col not in range(COLS):
            return 1
        
        if grid[row][col] == 0:
            return 1

        if (row, col) in visited:
            return 0
        
        visited.add((row, col))

        
        
        return self.traverseIslandAndCalculatePerimeter(row + 1, col, ROWS, COLS, visited, grid) + \
        self.traverseIslandAndCalculatePerimeter(row - 1, col, ROWS, COLS, visited, grid) + \
        self.traverseIslandAndCalculatePerimeter(row, col + 1, ROWS, COLS, visited, grid) + \
        self.traverseIslandAndCalculatePerimeter(row, col - 1, ROWS, COLS, visited, grid)
