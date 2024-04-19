class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        allSubsets = []

        def backtrack(i, subset):

            if i >= len(nums):
                allSubsets.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)
            
        backtrack(0, [])
        return allSubsets
        