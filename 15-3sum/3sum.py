class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        for i in range(len(nums)):

            # if we are at a positive number,
            # starting a triplet from here will never result in 0
            if nums[i] > 0:
                break
            
            # if we are at a number which is same as its left, 
            # then we have already found a triplet with this number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    triplets.add(tuple(sorted([nums[i], nums[l], nums[r]])))
                    l += 1
                    r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        
        return list(triplets)


        