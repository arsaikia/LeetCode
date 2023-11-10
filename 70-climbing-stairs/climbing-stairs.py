class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def dp(num):
            if num > n:
                return 0
            
            if num == n:
                return 1
            
            if num in cache:
                return cache[num]
            
            cache[num] = dp(num + 1) + dp(num + 2)
            return cache[num]
        
        return dp(0)
        