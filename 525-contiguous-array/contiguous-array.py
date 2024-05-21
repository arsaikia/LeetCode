class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        zeros, ones = 0, 0
        diffPrefix = {}
        res = 0

        for idx, num in enumerate(nums):
            if num:
                ones += 1
            else:
                zeros += 1
            
            diff = ones - zeros
            if diff not in diffPrefix:
                diffPrefix[diff] = idx
            
            if zeros == ones:
                res = zeros + ones
            else:
                res = max(res, idx - diffPrefix[diff])
        
        return res

        