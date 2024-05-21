class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = -1
        closest = float("inf")

        for i in range(len(nums)):

            num = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = num + nums[l] + nums[r]
                if closest > abs(total - target):
                    closest = abs(total - target)
                    res = total
                
                if total > target:
                    r-= 1
                else:
                    l += 1
        return res




        