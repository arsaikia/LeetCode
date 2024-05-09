class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = cost[:] + [0]

        for idx in range(2, len(dp)):
            dp[idx] += min(dp[idx - 1], dp[idx - 2])
        
        return dp[-1]
