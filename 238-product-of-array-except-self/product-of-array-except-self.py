class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplier = 1
        prefix = [1] * len(nums)
        for i in range(1, len(prefix)):
            prefix[i] = multiplier * nums[i - 1]
            multiplier = multiplier * nums[i - 1]
        
        suffixMultiplier = 1
        
        for i in reversed(range(len(prefix))):
            prefix[i] *= suffixMultiplier
            suffixMultiplier *= nums[i]
        
        return prefix




        