class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l, r = 0, len(nums) - 1
        maxPairSum = 0
        while l < r:
            left, right = nums[l], nums[r]
            pairSum = left + right
            maxPairSum = max(maxPairSum, pairSum)
            l += 1
            r -= 1
        
        return maxPairSum


        