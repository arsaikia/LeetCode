class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        nums.sort() # O(N log N)


        def backtracking(idx, subset):
            if idx >= len(nums):
                allSubsets.append(subset[:])   # O(N)
                return
            
            # include current number
            subset.append(nums[idx])
            backtracking(idx + 1, subset)

            # Do not include any number that is equal to curr
            subset.pop()
            while idx < len(nums) - 1 and nums[idx + 1] == nums[idx]:
                idx += 1
            backtracking(idx + 1, subset)
        
        backtracking(0, [])
        return allSubsets
