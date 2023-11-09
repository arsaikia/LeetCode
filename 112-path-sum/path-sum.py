# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.getPathSum(root, 0, targetSum)
    
    def getPathSum(self, node, pathSum, targetSum):
        if not node:
            return False

        pathSum += node.val
        if not node.left and not node.right:
            return pathSum == targetSum
        
        return (self.getPathSum(node.left, pathSum, targetSum) or
        self.getPathSum(node.right, pathSum, targetSum))

        