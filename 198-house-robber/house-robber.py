class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}

        def backtrack(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            # rob current
            rob = nums[i] + backtrack(i + 2)

            # skip current
            skip = backtrack(i + 1)

            cache[i] = max(rob, skip)
            return cache[i]

        return backtrack(0)