class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        current = []
        ans = []

        def backtracking(i, j):
            if i == len(s) or j > len(s) :
                if len(''.join(current)) == len(s):
                    ans.append(current[:])
                return

            substr = s[i:j]

            if substr == substr[::-1] and len(substr) > 0:
                current.append(substr)
                backtracking(j, j + 1)
                current.pop()

            backtracking(i,  j + 1)

        backtracking(0,0)
        return ans
        

            