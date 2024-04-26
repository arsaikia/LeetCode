class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        visited = set()

        @cache
        def backtrack(r, c):
            if r == len(grid) - 1:
                return grid[r][c]
            
            nextMin = float("inf")
            for i in range(len(grid)):
                if i != c:
                    nextMin = min(nextMin, backtrack(r + 1, i))

            return grid[r][c] + nextMin
        
        res = float("inf")
        for c in range(len(grid)):
            res = min(backtrack(0, c), res)

        return res



            

        