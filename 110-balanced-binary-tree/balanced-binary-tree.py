# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def isNodeBalanced(node):
            if not node:
                return (True, 0)
            
            isLeftBalanced, maxDepthLeft = isNodeBalanced(node.left)
            isRightBalanced, maxDepthRight = isNodeBalanced(node.right)

            isCurrBalanced = isLeftBalanced and isRightBalanced and abs(maxDepthLeft - maxDepthRight) < 2
            maxDepthCurr = 1 + max(maxDepthLeft, maxDepthRight)

            return (isCurrBalanced, maxDepthCurr)
        
        isBalanced, __ = isNodeBalanced(root)
        return isBalanced
        