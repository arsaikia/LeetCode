# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def merge(p, q):
            if not p and not q:
                return None
            
            if p and not q:
                return p
            
            elif not p and q:
                return q
            
            else:
                node = TreeNode()
                node.val = p.val + q.val
                node.left = merge(p.left, q.left)
                node.right = merge(p.right, q.right)
                return node
            
        return merge(root1, root2)

        