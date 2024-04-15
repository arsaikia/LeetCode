# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, sum):
            if not node:
                return 0
            
            currSum = (10 * sum) + node.val

            leftSum = dfs(node.left, currSum)
            rightSum = dfs(node.right, currSum)

            if not node.left and not node.right:
                return currSum

            return leftSum + rightSum
        
        return dfs(root, 0)
            
