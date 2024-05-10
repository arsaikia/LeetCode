class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        i = 0

        while i <= r:

            # found 0
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            
            # found 2
            elif nums[i] == 1:
                i += 1
            else:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
        
        return nums
            


            