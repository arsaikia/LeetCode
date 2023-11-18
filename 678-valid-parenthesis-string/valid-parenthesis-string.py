class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack1 = [] # Keeps track of open parenthesis
        stack2 = [] # Keeps track of stars
        for i,x in enumerate(s):
            if x == '*':
                stack2.append(i)
                continue
            if x == '(':
                stack1.append(i)
                continue
            if x == ')':
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
                else: return False
                
        while stack1 and stack2:
            if stack2[-1] > stack1[-1]:
                stack1.pop()
                stack2.pop()
            else:
                return False
            
        return not stack1