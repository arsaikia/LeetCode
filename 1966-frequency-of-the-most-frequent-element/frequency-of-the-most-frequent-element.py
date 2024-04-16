class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        sum = 0
        res = 0
        
        for r in range(len(nums)):
            sum += nums[r]

            while (r - l + 1) * nums[r] - sum > k:
                sum -= nums[l]
                l += 1
            
            if (r - l + 1) * nums[r] - sum <= k:
                res = max(res, (r - l + 1))
        
        return res
        