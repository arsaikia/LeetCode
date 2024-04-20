class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        lands, visited = [], set()
        ROWS, COLS = len(land), len(land[0])


        def dfs(rowIdx, colIdx, curr):
            if rowIdx not in range(ROWS) or colIdx not in range(COLS) or (rowIdx, colIdx) in visited:
                return
            
            visited.add( (rowIdx, colIdx) )
            if land[rowIdx][colIdx] == 0:
                return
            
            curr.append([rowIdx, colIdx])
            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                dfs(rowIdx + dr, colIdx + dc, curr)
            
            return curr
        

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in visited:
                    continue
                ret = dfs(row, col, [])
                if ret:
                    lands.append(ret)
        
        rect = []
        for land in lands:
            land.sort()
            rect.append([land[0][0], land[0][1], land[-1][0], land[-1][1]])
        
        return rect
        

        