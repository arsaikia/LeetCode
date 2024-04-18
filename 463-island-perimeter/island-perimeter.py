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

        perimeter = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            perimeter += self.traverseIslandAndCalculatePerimeter(row + dr, col + dc, ROWS, COLS, visited, grid)
        
        return perimeter
