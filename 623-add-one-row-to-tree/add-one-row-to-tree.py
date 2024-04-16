# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node, currDepth, val, isLeft):
            if not node:
                return

            if currDepth == depth - 1:
                nextLeft, nextRight = node.left, node.right
                newNode = TreeNode(val, nextLeft, None)
                node.left = newNode
                newNode = TreeNode(val, None, nextRight)
                node.right = newNode
            
            
            dfs(node.left, currDepth + 1, val, True)
            dfs(node.right, currDepth + 1, val, False)
        
        # base case
        if depth == 1:
            newNode = TreeNode(val)
            newNode.left = root
            return newNode

        dfs(root, 1, val, 0)
        return root