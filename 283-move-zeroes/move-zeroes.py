class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nonZeroIdx = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[nonZeroIdx], nums[i] = nums[i], nums[nonZeroIdx]
                nonZeroIdx += 1
        
        