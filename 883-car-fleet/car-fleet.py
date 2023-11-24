class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = []
        for idx in range(len(position)):
            pos.append( (position[idx], speed[idx], (target - position[idx]) / speed[idx]) )
        pos.sort()
        stack = []

        for p, s, timeRequired in reversed(pos):
            if stack and stack[-1] >= timeRequired:
                continue
            stack.append(timeRequired)
        
        return len(stack)

