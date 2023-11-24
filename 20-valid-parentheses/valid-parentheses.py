class Solution:
    def isValid(self, s: str) -> bool:

        stack = []


        for bracket in s:
            if bracket == ")" and stack and stack[-1] == "(":
                stack.pop()
            elif bracket == "}" and stack and stack[-1] == "{":
                stack.pop()
            elif bracket == "]" and stack and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(bracket)
        
        return len(stack) == 0

        