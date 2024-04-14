# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def binary(node, isLeft):
            if not node:
                return 0

            if node.left is None and node.right is None and isLeft:
                return node.val

            return binary(node.left, True) + binary(node.right, False)
        
        return binary(root, False)

        