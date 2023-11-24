class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, stack = [], []

        def backtracking(opening, closing):
            if opening == closing == n:
                res.append("".join(stack))
                return
            
            if opening < n:
                stack.append("(")
                backtracking(opening + 1, closing)
                stack.pop()
            
            if closing < opening:
                stack.append(")")
                backtracking(opening, closing + 1)
                stack.pop()
        
        backtracking(0, 0)
        return res
        