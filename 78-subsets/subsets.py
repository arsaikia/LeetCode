class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        
        def backtracking(nums, currIdx, subset):

            if currIdx >= len(nums):
                allSubsets.append(subset[:])
                return
            
            # include currIdx element
            subset.append(nums[currIdx])
            backtracking(nums, currIdx + 1, subset)


            # Do not include currIdx element
            subset.pop()
            backtracking(nums, currIdx + 1, subset)
        
        backtracking(nums, 0, [])

        return allSubsets
        