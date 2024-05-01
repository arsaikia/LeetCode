from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        EMPTY_CELL = "."
        visitedRows = defaultdict(set)  # {rowIdx : set() }
        visitedCols = defaultdict(set)  # {colIdx : set() }
        visitedGrids = defaultdict(set) # {(rowsIdx, colIdx) : set() }

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]

                if val == EMPTY_CELL:
                    continue
                
                if (
                    val in visitedRows[row] or
                    val in visitedCols[col] or
                    val in visitedGrids[(row // 3, col // 3)]
                ):
                    return False

                visitedRows[row].add(val)
                visitedCols[col].add(val)
                visitedGrids[(row // 3, col // 3)].add(val)
        
        return True

        