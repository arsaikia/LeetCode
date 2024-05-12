class Solution:
    def calculate(self, s: str) -> int:
        curr = res = 0
        sign = 1
        stack = []


        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            elif ch in ["+", "-"]:
                res += sign * curr
                sign = 1 if ch == "+" else -1
                curr = 0
            elif ch == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ")":
                res += curr * sign
                res *= stack.pop()
                res += stack.pop()
                curr = 0
        
        return res + curr * sign


        