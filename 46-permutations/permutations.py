class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = []
        used = [False] * len(nums)

        def backtrack(perm):
            if len(perm) == len(nums):
                return perms.append(perm[:])

            for idx in range(len(nums)):
                num = nums[idx]
                if not used[idx]:
                    used[idx] = True
                    perm.append(num)
                    backtrack(perm) 
                    perm.pop()
                    used[idx] = False
                    
        backtrack([])
        return perms
        