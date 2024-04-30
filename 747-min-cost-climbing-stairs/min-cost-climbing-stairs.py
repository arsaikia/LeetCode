class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0 for i in range(len(cost))]
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for idx in reversed(range(len(cost) - 2)):
            dp[idx] = cost[idx] + min(dp[idx + 1], dp[idx + 2])
        
        return min(dp[0], dp[1])

        