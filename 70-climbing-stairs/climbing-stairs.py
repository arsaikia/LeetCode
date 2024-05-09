class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def dfs(i):

            if i == n:
                return 1
            
            if i > n:
                return 0
            
            if i in dp:
                return dp[i]
            
            res = 0
            res += dfs(i + 1) + dfs(i + 2)
            dp[i] = res
            return dp[i]
        
        return dfs(0)