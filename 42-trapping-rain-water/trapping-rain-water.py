class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax = 0, 0
        l, r = 0, len(height) - 1
        maxRain = 0

        while l < r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])
            trapHeight = min(lMax, rMax)
            leftRain = trapHeight - height[l] if trapHeight - height[l] > 0 else 0
            rightRain = trapHeight - height[r] if trapHeight - height[r] > 0 else 0
            maxRain += leftRain + rightRain

            if height[l] > height[r]:
                
                r -= 1
            else:
                
                l += 1
        
        return maxRain

