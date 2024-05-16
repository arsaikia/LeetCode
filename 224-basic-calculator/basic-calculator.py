class Solution:
    def calculate(self, s: str) -> int:
        curr, res, sign, stack = 0, 0, 1, []

        for ch in s:
            if ch.isdigit():
                curr = (10 * curr) + int(ch)
            elif ch in "+-":
                res += curr * sign
                curr = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ")":
                res += curr * sign
                curr = 0

                res *= stack.pop()
                res += stack.pop()
        
        return res + curr * sign

        