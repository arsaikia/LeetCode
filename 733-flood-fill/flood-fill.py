class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS, COLS, visited = len(image), len(image[0]), set()


        q = collections.deque([(sr, sc, image[sr][sc])])

        while q:
            for i in range(len(q)):
                row, col, currColor = q.popleft()

                image[row][col] = color
                visited.add( (row, col))

                for nr, nc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    r = row + nr
                    c = col + nc
                    if r not in range(ROWS) or c not in range(COLS) or (r, c) in visited or image[r][c] != currColor:
                        continue
                    
                    q.append( (r, c, currColor))
        
        return image
                    
                    

        