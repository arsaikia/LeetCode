class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        
        def backtrack(idx, running):
            allSubsets.append(running[:])
            
            for i in range(idx, len(nums)):
                running.append(nums[i])
                backtrack(i + 1, running)
                running.pop()
            
        backtrack(0, [])
        return allSubsets