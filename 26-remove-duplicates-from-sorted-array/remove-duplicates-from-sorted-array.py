class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        lastUniqueIdx = 1
        for i in range(1, len(nums)):
            # found a unique pair
            if nums[i - 1] != nums[i]:
                nums[lastUniqueIdx] = nums[i]
                lastUniqueIdx += 1
        
        return lastUniqueIdx