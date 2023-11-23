class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        EMPTY_CELL = "."
        visitedRows = collections.defaultdict(set) # { rowsIdx }
        visitedCols = collections.defaultdict(set) # { rowsIdx }
        visitedGrids = collections.defaultdict(set) # { (rowsIdx // 3, ColsIdx // 3) }

        for row in range(len(board)):
            for col in range(len(board[0])):
                value = board[row][col]
                if value == EMPTY_CELL:
                    continue
                
                if value in visitedRows[row]:
                    return False
                if value in visitedCols[col]:
                    return False
                if value in visitedGrids[(row // 3, col // 3)]:
                    return False
                
                visitedRows[row].add(value)
                visitedCols[col].add(value)
                visitedGrids[(row//3,col//3)].add(value)
        
        return True