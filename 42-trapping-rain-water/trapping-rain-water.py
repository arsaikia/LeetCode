class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = 0, 0
        l, r = 0, len(height) - 1
        area = 0

        while l < r:
            left, right = height[l], height[r]
            minHeight = min(leftMax, rightMax)

            leftArea = minHeight - left if minHeight - left > 0 else 0
            rightArea = minHeight - right if minHeight - right > 0 else 0

            area = area + leftArea + rightArea

            leftMax = max(leftMax, left)
            rightMax = max(rightMax, right)

            if left < right:
                l += 1
            else:
                r -= 1
        
        return area


