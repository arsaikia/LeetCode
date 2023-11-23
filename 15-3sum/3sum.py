class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for idx in range(len(nums)):
            val = nums[idx]
            l, r = idx + 1, len(nums) - 1
            while l < r:
                small, large = nums[l], nums[r]
                if val + small + large == 0:
                    if tuple(sorted([val, small, large])) not in triplets:
                        triplets.add((val, small, large))
                    l += 1
                    r -= 1
                elif val + small + large > 0:
                    r -= 1
                else:
                    l += 1
        return triplets


