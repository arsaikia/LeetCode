class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        
        def backtrack(idx):
            subsets.append(subset[:])

            for i in range(idx, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()
            
        backtrack(0)

        return subsets