class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        visited = set()
        cache = {}

        def backtrack(row, col):
            nonlocal ROWS, COLS, visited

            if (row, col) in cache:
                return cache[(row, col)]

            if row not in range(ROWS) or col not in range(COLS) or (row, col) in visited:
                return 0
            
            if row == ROWS - 1 and col == COLS - 1:
                return 1
            
            visited.add( (row, col) )
            ways = 0
            ways += backtrack(row + 1, col) + backtrack(row, col + 1)
            visited.remove( (row, col) )
            
            cache[(row, col)] = ways
            return cache[(row, col)]
        
        return backtrack(0, 0)
        
