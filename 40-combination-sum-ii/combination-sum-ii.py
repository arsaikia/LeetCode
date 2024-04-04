class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        combinations = []

        def backtrack(idx, total, combination):

            # found a combindation that adds up to target
            if total == target:
                combinations.append(combination[:])
                return

            # Out of bounds
            if idx >= len(candidates) or total > target:
                return
            
            # Consider current element
            combination.append(candidates[idx])
            backtrack(idx + 1, total + candidates[idx], combination)

            # Do not include any elements matching curr value
            combination.pop()
            while idx + 1 < len(candidates) and candidates[idx + 1] == candidates[idx]:
                idx += 1
            backtrack(idx + 1, total, combination)
        
        backtrack(0, 0, [])
        return combinations
        