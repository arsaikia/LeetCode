# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minVal = float("inf")
        prev = None

        def inorder(node):
            nonlocal prev
            nonlocal minVal

            if not node:
                return float("inf")
            
            inorder(node.left)
            if prev:
                minVal = min(minVal, abs(node.val - prev.val))
            prev = node
            inorder(node.right)

            return minVal

            
        minValue = inorder(root)
        return minValue if minValue != float("inf") else -1
        