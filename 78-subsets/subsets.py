class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        subset = []
        
        def backtrack(idx):
            # if we have reached the end of list, we have used up all elements
            # we can save the subset to output
            if idx == len(nums):
                subsets.append(subset[:])
                return

            # include element in current Idx
            subset.append(nums[idx])
            backtrack(idx + 1)

            # do NOT iclude current element, try next one
            subset.pop()
            backtrack(idx + 1)
        
        backtrack(0)

        return subsets