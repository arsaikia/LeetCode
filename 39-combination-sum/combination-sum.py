class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i, total):

            if total == target:
                res.append(subset[:])
                return
            
            if total > target or i >= len(candidates):
                return
            
            for idx in range(i, len(candidates)):
                # consider curr element
                subset.append(candidates[idx])
                backtrack(idx, total + candidates[idx])
                # skip curr element
                subset.pop()
        
        backtrack(0, 0)
        return res
        