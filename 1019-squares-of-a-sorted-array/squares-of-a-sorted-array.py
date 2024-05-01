class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = collections.deque([])

        l, r = 0, len(nums) - 1

        while l <= r:
            left, right = nums[l] ** 2, nums[r] ** 2
            if left > right:
                res.appendleft(left)
                l += 1
            else:
                res.appendleft(right)
                r -= 1
        
        return res
        