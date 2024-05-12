class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        def findMax(startRow, startCol):
            maxVal = float("-inf")
            for i in range(startRow, startRow + 2 + 1):
                for j in range(startCol, startCol + 2 + 1):
                    maxVal = max(maxVal, grid[i][j])
            return maxVal
        
        
        res = [ [0 for col in range(len(grid) - 2)] for row in range(len(grid) - 2)]

        for row in range(len(res)):
            for col in range(len(res)):
                res[row][col] = findMax(row, col)
        
        return res

        