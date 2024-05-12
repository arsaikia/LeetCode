class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (idx, height)
        maxArea = 0

        for idx, h in enumerate(heights):
            startIdx = idx
            while stack and stack[-1][1] > h:
                lastIdx, lastHeight = stack.pop()
                maxArea = max(maxArea, lastHeight * (idx - lastIdx))
                startIdx = lastIdx
            stack.append([startIdx, h])

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea

        