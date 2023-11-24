class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for __ in temperatures]
        stack = []

        for idx, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                prevTemp, prevIdx = stack.pop()
                res[prevIdx] = idx - prevIdx
            
            stack.append( (temp, idx) )
        
        return res


        