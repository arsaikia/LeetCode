class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            
            # include curr num
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # skip curr num
            subset.pop()
            backtrack(i + 1, subset)
        
        backtrack(0, subset)
        return res
        