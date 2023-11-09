class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(i, subStr, total):
            if i >= len(candidates) or total > target:
                return

            if total == target:
                res.append(subStr[:])
                return
            
            # include
            subStr.append(candidates[i])
            dfs(i, subStr, total + candidates[i])

            # not include
            subStr.pop()
            dfs(i + 1, subStr, total)

        dfs(0, [], 0)
        return res