class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax = 0, 0
        l, r = 0, len(height) - 1
        rainCollected = 0

        while l < r:
            trapHeight = min(lMax, rMax)
            leftWater = trapHeight - height[l] if (trapHeight - height[l]) > 0 else 0
            rightWater = trapHeight - height[r] if (trapHeight - height[r]) > 0 else 0
            rainCollected += leftWater + rightWater

            lMax, rMax = max(lMax, height[l]), max(rMax, height[r])

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return rainCollected