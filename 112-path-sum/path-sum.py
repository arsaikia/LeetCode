# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSums = []
        self.getPathSum(root, pathSums, 0)

        for pathSum in pathSums:
            if pathSum == targetSum:
                return True
        return False
    
    def getPathSum(self, node, pathSums, currPathSum):
        if not node:
            return 0

        currPathSum += node.val
        if not node.left and not node.right:
            pathSums.append(currPathSum)
            currPathSum -= node.val
            return currPathSum
        
        self.getPathSum(node.left, pathSums, currPathSum)
        self.getPathSum(node.right, pathSums, currPathSum)

        