class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        combinations = []

        def backtrack(idx, total, combination):

            # found a combindation that adds up to target
            if total == target:
                combinations.append(combination[:])
                return

            # Out of bounds
            if idx >= len(candidates) or total > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                # Consider current element
                combination.append(candidates[i])
                backtrack(i + 1, total + candidates[i], combination)
                # Do not include any elements matching curr value
                combination.pop()

        
        backtrack(0, 0, [])
        return combinations
        