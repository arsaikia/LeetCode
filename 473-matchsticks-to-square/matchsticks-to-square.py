class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if isinstance(total % 4, float):
            return False

        matchsticks.sort(reverse=True)
        sides = {
            "top": 0,
            "bottom": 0,
            "left": 0,
            "right": 0
        }

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for edge in sides:
                if sides[edge] + matchsticks[i] <= total // 4:
                    sides[edge] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[edge] -= matchsticks[i]
            return False
        
        return backtrack(0)

        