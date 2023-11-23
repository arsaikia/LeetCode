class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(num, idx) for idx, num in enumerate(nums)]
        nums.sort()

        left, right = 0, len(nums) - 1

        while left < right:
            small = nums[left][0]
            big = nums[right][0]

            if small + big == target:
                return [nums[left][1], nums[right][1]]
            elif small + big > target:
                right -= 1
            else:
                left += 1
