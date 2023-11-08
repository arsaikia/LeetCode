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
        node[self.endSymbol] = word


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        trie = Trie(word)
        ROWS, COLS = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(row, col, node):
            if (
                row not in range(ROWS) or 
                col not in range(COLS) or
                (row, col) in visited  or
                board[row][col] not in node
                ):
                return
            
            visited.add((row, col))
            node = node[board[row][col]]

            if "*" in node:
                res.add(node["*"])

            dfs(row + 1, col, node)
            dfs(row, col + 1, node)
            dfs(row - 1, col, node)
            dfs(row, col - 1, node)

            visited.remove((row, col))
        

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, trie.root)
        
        return list(res)

        