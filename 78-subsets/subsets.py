class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.backtrack(nums, 0, [], subsets)
        return subsets
    
    def backtrack(self, nums, idx, subset, subsets):
        if idx >= len(nums):
            subsets.append(subset[:])
            return
        
        subset.append(nums[idx])
        self.backtrack(nums, idx + 1, subset, subsets)

        subset.pop()
        self.backtrack(nums, idx + 1, subset, subsets)
        