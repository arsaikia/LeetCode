class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idx = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                count += 1
            else:
                count = 1
            

            if count <= 2:
                nums[idx] = nums[i]
                idx += 1
        
        return idx