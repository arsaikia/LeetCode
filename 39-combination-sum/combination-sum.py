class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def backtracking(idx, total, candidate):
            if idx >= len(candidates) or total > target:
                return
            
            if total == target:
                combinations.append(candidate[:])
                return
            
            # consider current num
            candidate.append(candidates[idx])
            total += candidates[idx]
            backtracking(idx, total, candidate)

            # skip current
            candidate.pop()
            total -= candidates[idx]
            backtracking(idx + 1, total, candidate)
        
        backtracking(0, 0, [])
        return combinations