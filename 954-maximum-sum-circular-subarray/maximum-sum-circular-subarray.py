class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax, currMin, globalMax, globalMin = 0, 0, nums[0], nums[0]

        i = 0

        for i in range(len(nums)):
            currMax = max(nums[i], currMax + nums[i])
            currMin = min(currMin + nums[i], nums[i])
            globalMax = max(globalMax, currMax)
            globalMin = min(globalMin, currMin)
            
        return max(globalMax, sum(nums) - globalMin) if globalMax > 0 else globalMax

        