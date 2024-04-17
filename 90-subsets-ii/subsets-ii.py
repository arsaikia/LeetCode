class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []

        def backtrack(idx, subset):
            if idx == len(nums):
                subsets.append(subset[:])
                return
            
            # add current element to subset
            subset.append(nums[idx])
            backtrack(idx + 1, subset)

            # do not include current to subset
            # HERE - because we have duplicates, the next might be same as previous
            # So a path that does not contain an element, it also can't contain any of its possible duplicates
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            subset.pop()
            backtrack(idx + 1, subset)

        backtrack(0, [])
        return subsets

