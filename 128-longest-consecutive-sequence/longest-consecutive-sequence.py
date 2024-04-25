class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        
        maxLongest = 0


        for num in nums:
            if num - 1 in values:
                continue
            longest = 0
            while num in values:
                longest += 1
                num += 1
            maxLongest = max(maxLongest, longest)
        
        return maxLongest

        