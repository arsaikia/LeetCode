class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xors = 0
        subsets = []

        def xor(a, b):
            return a ^ b

        def backtrack(i, subset):
            if i >= len(nums):
                subsets.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            backtrack(i + 1, subset)
        
        backtrack(0, [])
        for subset in subsets:
            currXor = 0 if not len(subset) else subset[0]
            for i in range(1, len(subset)):
                currXor = currXor ^ subset[i]
            xors = xors + currXor
        return xors
            
