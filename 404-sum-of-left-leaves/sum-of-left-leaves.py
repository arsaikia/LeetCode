# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self, res=0):
        self.res = res
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def binary(node, isLeft):
            if node.left is None and node.right is None and isLeft:
                self.res += node.val
            
            if node.left:
                binary(node.left, True)
            
            if node.right:
                binary(node.right, False)
        
        binary(root, False)
        return self.res

        