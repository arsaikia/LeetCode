# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(node, val):

            if not node:
                return None
            
            node.left = dfs(node.left, val)
            node.right = dfs(node.right, val)

            if node.left == node.right and node.val == val:
                return None

            return node
        
        return dfs(root, target)
        