class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = [__ for __ in s]

        stack = []
        res = []

        for idx, ch in enumerate(chars):
            if ch == ")":
                if stack and stack[-1] > 0:
                    stack.pop()
                else:
                    stack.append(-1 * (idx + 1))
            elif ch == "(":
                stack.append(idx + 1)

        print(stack)

        for i in stack:
            chars[abs(i) - 1] = -1
        
        for ch in chars:
            if ch != -1:
                res.append(ch)
            
        return "".join(res)
        