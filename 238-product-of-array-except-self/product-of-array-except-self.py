class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftMult = [1 for __ in nums]
        rightMult = [1 for __ in nums]

        runningMult = 1
        for idx in range(1, len(leftMult)):
            runningMult = nums[idx - 1] * runningMult
            leftMult[idx] = runningMult
        
        runningMult = 1
        for idx in reversed(range(len(rightMult) - 1)):
            runningMult = nums[idx + 1] * runningMult
            rightMult[idx] = runningMult
        
        res = [1 for __ in nums]

        for idx in range(len(nums)):
            res[idx] = leftMult[idx] * rightMult[idx]
        
        return res


        