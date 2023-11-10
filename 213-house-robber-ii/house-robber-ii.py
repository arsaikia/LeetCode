class Solution:
    def robber(self, nums: List[int]) -> int:
        secondLast = 0
        last = 0

        for i in range(len(nums)):
            tmp = max(nums[i] + secondLast, last)
            secondLast = last
            last = tmp

        return last

    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.robber(nums[1:]), self.robber(nums[:-1]))
        