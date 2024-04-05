class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        subsets = []

        def backtrack(idx, subset):
            if idx == len(nums):
                subsets.append(subset[:])
                return 
            
            # consider curr elements
            subset.append(nums[idx])
            backtrack(idx + 1, subset)

            # do not consider any elements same as current
            subset.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            backtrack(idx + 1, subset)
        
        backtrack(0, [])
        return subsets
        