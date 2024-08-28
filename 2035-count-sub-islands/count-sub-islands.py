class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ROW, COL = len(grid1), len(grid1[0])
        islandCount = 0

        # Traverse land in grid2 that can't create subislands and remove them
        for row in range(ROW):
            for col in range(COL):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    self.traverseAndRemove(grid1, grid2, row, col)
        
        # Traverse and get island from grid2
        for row in range(ROW):
            for col in range(COL):
                if grid2[row][col] == 1:
                    self.traverseAndRemove(grid1, grid2, row, col)
                    islandCount += 1
        return islandCount
    
    def traverseAndRemove(self, grid1, grid2, row, col):
        ROW, COL = len(grid1), len(grid1[0])
        if row not in range(ROW) or col not in range(COL) or grid2[row][col] == 0:
            return
        
        grid2[row][col] = 0

        for r, c in [[row + 1, col], [row, col + 1], [row - 1, col], [row, col - 1]]:
            self.traverseAndRemove(grid1, grid2, r, c)
        