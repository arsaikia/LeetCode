class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, subStr, total):

            # Base case: Positive: Out of bounds
            if i >= len(candidates) or total > target:
                return

            # Base case: Negative: nums add up to target
            if total == target:
                res.append(subStr[:])
                return
            
            # Include num in subset
            subStr.append(candidates[i])
            dfs(i, subStr, total + candidates[i])

            # Do not include num in subset
            subStr.pop()
            dfs(i + 1, subStr, total)

        dfs(0, [], 0)
        return res