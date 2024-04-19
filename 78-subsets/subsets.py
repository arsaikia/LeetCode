class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        allSubsets = []

        def backtrack(idx, subset):
            allSubsets.append(subset[:])
            
            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
            
        backtrack(0, [])
        return allSubsets
        