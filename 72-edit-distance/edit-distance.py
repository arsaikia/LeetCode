class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = {(len(word1), len(word2)): 0}
        
        def dfs(i, j):

            if (i, j) in dp:
                return dp[(i, j)]

            if i == len(word1) and j == len(word2):
                return 0
            
            elif i == len(word1):
                return len(word2) - j
            
            elif j == len(word2):
                return len(word1) - i
            
            val = float("inf")

            if word1[i] == word2[j]:
                val = min(val, dfs(i + 1, j + 1))
            else:
                insert = 1 + dfs(i, j + 1)
                replace = 1 + dfs(i + 1, j + 1)
                delete = 1 + dfs(i + 1, j)
                val = min(val, insert, replace, delete)
            
            dp[(i, j)] = val
            return val
        
        return dfs(0, 0)
            


        
