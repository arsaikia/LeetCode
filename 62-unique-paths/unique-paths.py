class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m, n
        memo = [ [0 for col in range(n + 1)] for row in range(m + 1) ]
        memo[m - 1][n - 1] = 1

        
        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if row == m - 1 and col == n - 1:
                    continue
                memo[row][col] = memo[row + 1][col] + memo[row][col + 1]
        
        return memo[0][0]

        