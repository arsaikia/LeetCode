class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPali(s, i, j):
            print(i, j, s[i:j])
            while i < j and j < len(s):
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        current = []
        ans = []

        def backtracking(i, j):
            if i == len(s) or j > len(s) :
                if len(''.join(current)) == len(s):
                    ans.append(current[:])
                return

            if isPali(s, i, j - 1) and j - i > 0:
                current.append(s[i:j])
                backtracking(j, j + 1)
                current.pop()

            backtracking(i,  j + 1)

        backtracking(0,0)
        return ans
        

            