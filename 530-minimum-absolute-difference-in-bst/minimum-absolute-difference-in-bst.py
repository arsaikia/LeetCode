# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        minDiff = float("inf")
        prev = None

        def inorder(node):
            nonlocal prev
            nonlocal minDiff

            if not node:
                return float("inf")
            
            inorder(node.left)

            if prev:
                minDiff = min(minDiff, abs(node.val - prev.val))
            
            prev = node
            inorder(node.right)
            return minDiff
        
        res =  inorder(root)
        return res if res != float("inf") else -1