class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, subarrayLength = 0, float("inf")
        runningSum = 0


        for r in range(len(nums)):
            # expand window
            runningSum += nums[r]

            # close window
            while runningSum >= target:
                subarrayLength = min(subarrayLength, r - l + 1)
                runningSum -= nums[l]
                l += 1
        
        return subarrayLength if subarrayLength != float("inf") else 0
        