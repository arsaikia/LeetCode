class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        
        def topDownDP(i, j):

            if i == len(s1) and j == len(s2) and i + j == len(s3):
                return True
            
            if (i, j) in cache:
                return cache[(i, j)]

            if i < len(s1) and i + j < len(s3) and s1[i] == s3[i + j] and topDownDP(i + 1, j):
                return True

            if j < len(s2) and i + j < len(s3) and s2[j] == s3[i + j] and topDownDP(i, j + 1):
                return True
            
            cache[(i, j)] = False
            
            return False
            
        return topDownDP(0, 0)
