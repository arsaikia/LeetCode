class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        return self.N_sum(nums,target,4)
        
    def N_sum(self, nums, target, n):
        if n == 2:
            return self.TwoSum(nums,target)
        else:
            res = []
            prev = None
            for i in range(len(nums)-n+1):
                if nums[i] != prev:                   
                    cur_sum = self.N_sum(nums[i+1:],target-nums[i],n-1)
                    for j in cur_sum:
                        j.append(nums[i])
                    res.extend(cur_sum)
                    prev = nums[i]
                
            return res
                
        
    def TwoSum(self, nums, target):
        L = 0
        R = len(nums)-1
        res = []
        while L < R:
            temp = nums[L] + nums[R]
            if temp == target:
                res.append([nums[L],nums[R]])
                L += 1
                R -= 1
                while L<R and nums[L] == nums[L-1]:
                    L += 1
                while L<R and nums[R] == nums[R+1]:
                    R -= 1
            elif temp < target:
                L += 1
            elif temp > target:
                R -= 1
        return res