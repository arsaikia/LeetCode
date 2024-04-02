class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            left, right = height[l], height[r]
            width = r - l
            hei = min(left, right)
            area = width * hei
            maxArea = max(maxArea, area)

            if left < right:
                l += 1
            else:
                r -= 1
        
        return maxArea