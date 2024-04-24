# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        found = {p: False, q: False}

        def dfs(node, p, q):
            if not node:
                return None
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if node == p:
                found[p] = True
                return node
            
            if node == q:
                found[q] = True
                return node
            
            if left and right:
                return node
            
            if left:
                return left
            
            if right:
                return right
            
            return None

        res = dfs(root, p, q)
        
        return res if res and (found[p] and found[q]) else None
            


        