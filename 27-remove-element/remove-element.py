class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach:
        # Starting at the begining of the array, keep moving until you find element same as val.
        # For non vals, swap

        position = 0

        for i in range(len(nums)):
            num = nums[i]
            if num == val:
                continue
            nums[i], nums[position] = nums[position], nums[i]
            position += 1
        
        return position
        