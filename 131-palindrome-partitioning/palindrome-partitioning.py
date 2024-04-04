class Solution:
    def partition(self, s: str) -> List[List[str]]:
        parts = []

        def isPali(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        def backtracking(i, part):
            if i >= len(s):
                parts.append(part[:])
                return
            
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    part.append(s[i : j + 1])
                    backtracking(j + 1, part)
                    part.pop()
        
        backtracking(0, [])
        return parts


        