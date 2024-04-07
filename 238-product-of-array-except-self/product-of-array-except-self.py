class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i - 1] * nums[i - 1]
        
        postfixMultiplier = 1

        for idx in reversed(range(len(nums))):
            prefixes[idx] = postfixMultiplier * prefixes[idx]
            postfixMultiplier *= nums[idx]
        
        return prefixes