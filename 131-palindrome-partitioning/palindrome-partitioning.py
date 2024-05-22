class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def isPali(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def backtrack(i, subset):
            if i >= len(s):
                res.append(subset[:])
                return
            
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    subset.append(s[i : j + 1])
                    backtrack(j + 1, subset)
                    subset.pop()
        
        backtrack(0, [])
        return res
        