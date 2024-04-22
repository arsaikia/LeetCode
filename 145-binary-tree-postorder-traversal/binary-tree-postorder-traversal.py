# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, res = [(root, False)], []

        while stack:
            node, isVisited = stack.pop()
            if not node:
                continue

            if isVisited:
                res.append(node.val)
                continue

            stack.append( (node, True) )        
            stack.append( (node.right, False) )        
            stack.append( (node.left, False) )

        return res        