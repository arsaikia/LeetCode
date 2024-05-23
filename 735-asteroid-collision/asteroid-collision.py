class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        res = []
        
        for a in asteroids:
            # add posiive asteroids
            if a > 0:
                stack.append(a)
                continue
            
            # negative destroys positive from stack
            while stack and stack[-1] > 0 and stack[-1] < abs(a):
                stack.pop()

            # negative desroyed everything
            if len(stack) == 0:
                res.append(a)
            
            # last positive > curr negative
            else:
                # both equal
                if stack[-1] == abs(a):
                    stack.pop()

        return res + stack