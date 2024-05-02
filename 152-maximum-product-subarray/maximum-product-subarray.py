class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = 1
        minProduct = 1
        res = nums[0]


        for num in nums:
            currMax = maxProduct * num
            currMin = minProduct * num

            maxProduct = max(num, currMax, currMin)
            minProduct = min(num, currMax, currMin)

            res = max(res, maxProduct)
        
        return res
        