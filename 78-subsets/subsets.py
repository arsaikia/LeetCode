class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        running = []
        
        def backtrack(idx):
            allSubsets.append(running[:])
            
            for i in range(idx, len(nums)):
                running.append(nums[i])
                backtrack(i + 1)
                running.pop()
            
        backtrack(0)
        return allSubsets