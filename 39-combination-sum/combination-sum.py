class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i, total, subset):

            if total == target:
                res.append(subset[:])
                return
            
            if total > target or i >= len(candidates):
                return
            
            # include current num
            subset.append(candidates[i])
            backtrack(i, total + candidates[i], subset)

            # skip current
            subset.pop()
            backtrack(i + 1, total, subset)
                    
        backtrack(0, 0, subset)
        return res
                
        