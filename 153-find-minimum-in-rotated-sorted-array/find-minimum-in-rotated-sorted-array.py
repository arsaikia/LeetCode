class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:
            # if the array from [l : r] is already sorted we can return the leftmost element
            if nums[l] <= nums[r]:
                return nums[l]
            
            m = l + ((r - l) // 2)
            # if the [l : m] subarray is not sorted, we have start of rotation here, search here next
            if nums[l] > nums[m]:
                r = m
            else:
                l = m + 1
        
            
        