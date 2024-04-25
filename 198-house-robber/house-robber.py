class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums) + 2)]

        for i in reversed(range(len(nums))):
            dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
        
        return dp[0]