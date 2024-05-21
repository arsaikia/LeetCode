class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0


        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                one, two, three = nums[i], nums[l], nums[r]
                total = one + two + three

                if total < target:
                    res += r - l
                    l += 1
                
                else:
                    r -= 1
        
        return res
        