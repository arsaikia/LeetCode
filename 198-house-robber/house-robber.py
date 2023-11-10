class Solution:
    def rob(self, nums: List[int]) -> int:
        secondLast = 0
        last = 0

        for i in range(len(nums)):
            tmp = max(nums[i] + secondLast, last)
            secondLast = last
            last = tmp

        return last

        