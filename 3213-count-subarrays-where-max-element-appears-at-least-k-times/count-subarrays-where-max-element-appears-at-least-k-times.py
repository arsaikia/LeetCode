class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxValue = max(nums)
        occurance = 0
        l = 0
        res = 0

        for r in range(len(nums)):
            if nums[r] == maxValue:
                occurance += 1
            
            while occurance > k or (l <= r and occurance == k and nums[l] != maxValue ):
                if nums[l] == maxValue:
                    occurance -= 1
                l += 1
            
            if occurance == k:
                res += l + 1
            
        return res

        