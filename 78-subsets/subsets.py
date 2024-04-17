class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        
        def backtrack(idx, running):
            if idx == len(nums):
                allSubsets.append(running[:])
                return
            
            running.append(nums[idx])
            backtrack(idx + 1, running)
            running.pop()
            backtrack(idx + 1, running)
        
        backtrack(0, [])
        return allSubsets