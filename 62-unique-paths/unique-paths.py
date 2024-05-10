class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLS = m + 1, n + 1
        prevRow = [0] * COLS
        currRow = [0] * COLS

        # base case
        currRow[COLS - 1] = 1

        for __ in reversed(range(ROWS - 1)):
            for col in reversed(range(COLS - 1)):
                currRow[col] = currRow[col + 1] + prevRow[col]
            prevRow = currRow
            currRow = [0] * COLS
        
        return prevRow[0]
        