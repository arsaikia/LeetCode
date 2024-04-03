class Trie:
    def __init__(self, word):
        self.root = {}
        self.endSymbol = "*"
        self.insert(word)

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.endSymbol] = True

class Solution:
        
    def backtrack(self, row, col, grid, visited, node):
        ROWS = len(grid)
        COLS = len(grid[0])

        if (row not in range(ROWS) or col not in range(COLS) or (row, col) in visited):
            return False

        char = grid[row][col]

        if char not in node:
            return False

        visited.add((row, col))
        node = node[char]

        if "*" in node:
            return True
        
        found = (
            self.backtrack(row + 1, col, grid, visited, node) or
            self.backtrack(row - 1, col, grid, visited, node) or
            self.backtrack(row, col + 1, grid, visited, node) or
            self.backtrack(row, col - 1, grid, visited, node)
        )

        if found:
            return True

        visited.remove((row, col))
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        trie = Trie(word)
        root = trie.root
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        for row in range(ROWS):
            for col in range(COLS):
                wordExists = self.backtrack(row, col, board, visited, root)
                if wordExists:
                    return True
        
        return False
        
        