class Trie:
    def __init__(self, words):
        self.root = {}
        self.endSymbol = "*"
        
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node[self.endSymbol] = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie(words)
        for word in words:
            trie.insert(word)

        finalWords = []
        visited = set()
        ROWS, COLS = len(board), len(board[0])

        def explore(row, col, node):
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                (row, col) in visited or
                board[row][col] not in node
            ):
                return

            nextNode = node[board[row][col]]

            visited.add((row, col))

            if trie.endSymbol in nextNode:
                finalWords.append(nextNode[trie.endSymbol])
                del nextNode[trie.endSymbol]
            
            explore(row + 1, col, nextNode)
            explore(row - 1, col, nextNode)
            explore(row, col + 1, nextNode)
            explore(row, col - 1, nextNode)

            visited.remove((row, col))

            # important to avoid TLE
            if not nextNode:
                node.pop(board[row][col])


        for row in range(ROWS):
            for col in range(COLS):
                explore(row, col, trie.root)

        return finalWords
        