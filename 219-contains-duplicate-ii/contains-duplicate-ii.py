class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        inWindow = set()
        l = 0

        for r in range(len(nums)):

            # close window if in window elements size > k
            while r - l > k:
                inWindow.remove(nums[l])
                l += 1
            
            # opn window
            if nums[r] in inWindow:
                return True
            inWindow.add(nums[r])
        
        return False

        