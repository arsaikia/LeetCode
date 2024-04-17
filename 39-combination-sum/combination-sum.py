class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse = True)
        combinations = []

        def backtrack(idx, combination, total):
            if total == target:
                combinations.append(combination[:])
                return

            if idx >= len(candidates) or total > target:
                return
            
            combination.append(candidates[idx])
            backtrack(idx, combination, total + candidates[idx])

            combination.pop()
            backtrack(idx + 1, combination, total)
        
        backtrack(0, [], 0)
        return combinations
