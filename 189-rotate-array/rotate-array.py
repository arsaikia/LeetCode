class Solution:
    def swap(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        
        self.swap(nums, 0, len(nums) - 1)

        self.swap(nums, 0, k - 1)
        
        self.swap(nums, k, len(nums) - 1)
        
        
