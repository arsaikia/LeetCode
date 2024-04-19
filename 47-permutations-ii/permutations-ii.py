class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts = collections.Counter(nums)
        perms = []

        def backtrack(perm):
            if len(perm) == len(nums):
                perms.append(perm[:])
                return
            
            for num in counts:
                if counts[num] == 0:
                    continue
                
                if num in perms:
                    continue
                
                perm.append(num)
                counts[num] -= 1
                backtrack(perm)

                perm.pop()
                counts[num] += 1
        
        backtrack([])
        return perms