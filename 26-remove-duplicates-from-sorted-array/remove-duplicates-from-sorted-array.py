class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Approach:
        # Similar to move all 0's to the end of array,
        # In this problem, rather than removing duplicates, we move all unique elements to
        # the begining of the list

        # List with 1 element will always be unique
        # Set duplicate is found at idx = 1
        duplicateElementIdx = 1
        for i in range(1, len(nums)):
            # found a unique pair
            # For every unique pair, move the unique element to the last duplicate element idx
            if nums[i - 1] != nums[i]:
                nums[duplicateElementIdx] = nums[i]
                duplicateElementIdx += 1
        
        return duplicateElementIdx