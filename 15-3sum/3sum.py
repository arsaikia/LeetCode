class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for idx, num in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            while l < r:
                left, right = nums[l], nums[r]
                val = num + left + right
                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    triplet = tuple(sorted([num, left, right]))
                    triplets.add(triplet)
                    l += 1
                    r -= 1
        
        return list(triplets)
        