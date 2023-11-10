class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        allValidBoards = []
        visitedCols = set()
        visitedPositiveDiagonals = set()    # ( row + col )
        visitedNegativeDiagonals = set()    # ( row - col )
        board = [ ["." for col in range(n)] for row in range(n) ]

        def backtracking(row):
            # Base Condition
            if row == n:
                queenPositions = board.copy()
                queenPositions = ["".join(row) for row in queenPositions]
                allValidBoards.append(queenPositions)
                return
            
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
                board[row][col] = "Q"

                backtracking(row + 1)

                visitedCols.remove(col)
                visitedPositiveDiagonals.remove(row + col)
                visitedNegativeDiagonals.remove(row - col)
                board[row][col] = "."

        backtracking(0)
        return allValidBoards


        