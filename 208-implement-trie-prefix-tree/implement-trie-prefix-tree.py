class Trie:

    def __init__(self):
        self.trie = {}
        self.endSymbol = "*"
        

    def insert(self, word: str) -> None:
        node = self.trie

        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.endSymbol] = True
        

    def search(self, word: str) -> bool:
        node = self.trie

        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        
        return self.endSymbol in node
        

    def startsWith(self, prefix: str) -> bool:
        node = self.trie

        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)