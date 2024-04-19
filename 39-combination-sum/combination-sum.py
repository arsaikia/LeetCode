class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets = []
        candidates.sort(reverse=True)

        def backtrack(i, nums, subset, total):
            if i >= len(nums) or total >= target:
                if total == target:
                    subsets.append(subset[:])
                return

            subset.append(nums[i])
            backtrack(i, nums, subset, total + nums[i])
            subset.pop()
            backtrack(i + 1, nums, subset, total)
        
        backtrack(0, candidates, [], 0)
        
        return subsets