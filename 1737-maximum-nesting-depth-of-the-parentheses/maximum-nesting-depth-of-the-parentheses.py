class Solution:
    def maxDepth(self, s: str) -> int:
        maxDepth = 0
        currDepth = 0

        for ch in s:
            if ch == ")":
                currDepth -= 1
            
            if ch == "(":
                currDepth += 1
            
            maxDepth = max(currDepth, maxDepth)
        
        return maxDepth
            

        