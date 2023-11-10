class Solution:
    def totalNQueens(self, n: int) -> int:
        allValidBoards = 0
        visitedCols = set()
        visitedPositiveDiagonals = set()    # ( row + col )
        visitedNegativeDiagonals = set()    # ( row - col )

        def backtracking(row):

            # Base Condition
            if row == n:
                return 1

            validBoards = 0

            for col in range(n):
                if (
                    col in visitedCols or
                    (row + col) in visitedPositiveDiagonals or
                    (row - col) in visitedNegativeDiagonals
                ):
                    continue

                visitedCols.add(col)
                visitedPositiveDiagonals.add(row + col)
                visitedNegativeDiagonals.add(row - col)

                validBoards += backtracking(row + 1)

                visitedCols.remove(col)
                visitedPositiveDiagonals.remove(row + col)
                visitedNegativeDiagonals.remove(row - col)

            return validBoards

        return backtracking(0)