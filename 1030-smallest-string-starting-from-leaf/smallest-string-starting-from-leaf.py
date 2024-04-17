# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        allStrs = []

        def dfs(node, running):
            if not node:
                return
            
            running.append(node.val)

            if not node.left and not node.right:
                allStrs.append(running[::-1])
            
            dfs(node.left, running)
            dfs(node.right, running)
            running.pop()
        
        dfs(root, [])
        
        smallest = allStrs[0]
        
        for i in range(1, len(allStrs)):
            curr = allStrs[i]
            if curr < smallest:
                smallest = curr
        
        for i in range(len(smallest)):
            smallest[i] = chr(ord("a") + smallest[i])
        
        return "".join(smallest)
        