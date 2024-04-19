class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        perms = []

        def backtrack(perm):
            if len(perm) == len(nums):
                return perms.append(perm[:])

            for num in nums:
                if num not in perm:
                    perm.append(num)
                    backtrack(perm) 
                    perm.pop()
        backtrack([])
        return perms
        