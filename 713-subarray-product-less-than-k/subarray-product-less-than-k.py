class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        product = 1
        l = 0

        for r in range(len(nums)):
            product *= nums[r]

            # close window
            while l <= r and product >= k:
                product = product // nums[l]
                l += 1
            
            res += (r - l + 1)
        return res