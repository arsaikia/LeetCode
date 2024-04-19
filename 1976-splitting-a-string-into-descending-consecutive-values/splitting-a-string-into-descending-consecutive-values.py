class Solution:
    def splitString(self, s: str) -> bool:
        

        def backtrack(i, nums):
            if i == len(s) and len(nums) > 1:
                return True
            
            for j in range(i, len(s)):
                num = int(s[i : j + 1])
                if len(nums) and nums[-1] - num != 1:
                    continue
                nums.append(num)
                if backtrack(j + 1, nums):
                    return True
                nums.pop()
            return False
        
        return backtrack(0, [])


