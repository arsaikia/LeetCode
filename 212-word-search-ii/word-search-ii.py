class Trie:
    def __init__(self, words):
        self.root = {}
        self.endSymbol = "*"
        for word in words:
            self.insert(word)
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.endSymbol] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS, visited = len(board), len(board[0]), set() 
        res = []

        def find(row, col, visited, node):
            nonlocal ROWS, COLS
            if row not in range(ROWS) or col not in range(COLS) or (row, col) in visited or board[row][col] not in node:
                return
            
            visited.add((row, col))
            nextNode = node[board[row][col]]

            if "*" in nextNode:
                res.append(nextNode["*"])
                del nextNode["*"]
            
            find(row + 1, col, visited, nextNode)
            find(row - 1, col, visited, nextNode)
            find(row, col + 1, visited, nextNode)
            find(row, col - 1, visited, nextNode)
            visited.remove((row, col))

            if not nextNode:
                node.pop(board[row][col])
        
        trie = Trie(words)
        for r in range(ROWS):
            for c in range(COLS):
                find(r, c, visited, trie.root)
        return res


            
        