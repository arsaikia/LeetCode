class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLength = 0
        left, right = 0, 0

        for c in s:
            if c == "(":
                left += 1
            elif c == ")":
                right += 1
            
            if left == right:
                maxLength = max(maxLength, right * 2)
            elif right > left:
                left = 0
                right = 0
            
        left, right = 0, 0

        for i in reversed(range(len(s))):
            c = s[i]
            if c == "(":
                left += 1
            elif c == ")":
                right += 1
            
            if left == right:
                maxLength = max(maxLength, left * 2)
            elif left > right:
                left = 0
                right = 0
        
        return maxLength
            

        