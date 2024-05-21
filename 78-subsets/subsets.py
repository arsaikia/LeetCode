class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i, subset):
            res.append(subset[:])
            
            for j in range(i, len(nums)):
                # include curr num
                subset.append(nums[j])
                backtrack(j + 1, subset)
                # skip curr num
                subset.pop()
        
        backtrack(0, subset)
        return res
        