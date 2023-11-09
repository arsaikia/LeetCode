class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def backtrack(idx, subset):

            if idx == len(nums):
                subsets.append(subset[::])
                return
            
            # include the num
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()

            # Do not include num
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1

            backtrack(idx + 1, subset)
        
        backtrack(0, [])

        return subsets
            
        