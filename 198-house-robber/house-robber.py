class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
            
        dp = [nums[0]] + [max(nums[0], nums[1])] + [0 for i in range(len(nums) - 2)]

        for i in range(2, len(nums)):
            first = dp[i - 2]
            second = dp[i - 1]
            curr = nums[i]

            dp[i] = max(first, second, first + curr)
        
        return dp[len(nums) - 1]