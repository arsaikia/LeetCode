class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {} # (idx, total)

        def findWays(idx, totalSoFar):

            # Base Case
            if idx == len(nums):
                return 1 if totalSoFar == target else 0
            
            if (idx, totalSoFar) in dp:
                return dp[(idx, totalSoFar)]
            
            # Recursion
            dp[(idx, totalSoFar)] = (
                findWays(idx + 1, totalSoFar + nums[idx]) + 
                findWays(idx + 1, totalSoFar - nums[idx]))
            
            return dp[(idx, totalSoFar)]
        
        return findWays(0, 0)

        