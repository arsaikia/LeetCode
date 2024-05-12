class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        matrix = [row[:] for row in mat]
        m = len(matrix)
        n = len(matrix[0])
        q = deque()
        seen = set()
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    q.append((row, col, 0))
                    seen.add((row, col))
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while q:
            row, col, steps = q.popleft()
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r not in range(m) or c not in range(n) or (r, c) in seen:
                    continue
                seen.add( (r, c) )
                q.append( (r, c, 1 + steps))
                matrix[r][c] = steps + 1
        
        return matrix

