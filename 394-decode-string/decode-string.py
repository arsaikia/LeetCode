class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
                continue
            
            # build string until we find the opening [
            stringQ = collections.deque([])
            while stack[-1] != "[":
                char = stack.pop()
                stringQ.appendleft(char)
            
            # pop once aain to remove [
            stack.pop()

            # get the digit
            numQ = collections.deque([])
            while stack and stack[-1].isdigit():
                numQ.appendleft(stack.pop())
            
            currStr = int("".join(numQ)) * "".join(stringQ)
            stack.append(currStr)
        
        return "".join(stack)